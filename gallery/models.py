from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from PIL import Image as PilImage
import cv2


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Coloring_Page = models.ImageField(upload_to='coloring_pages', null=True)
    Original_Image = models.ImageField(upload_to='original_images', verbose_name='Image')
    sigma = models.DecimalField(max_digits=10, decimal_places=0, default=6, null=False, verbose_name='Focus')
    date_posted = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the Original Image and manipulate with OpenCV
        img = cv2.imread(self.Original_Image.path, 0)
        sigma = self.sigma
        mask = cv2.GaussianBlur(255 - img, (0, 0), sigma)
        img = cv2.divide(img, 255 - mask, scale=255)

        # Convert Image to to Pillow Image and resize
        img = PilImage.fromarray(img)

        # Resize if necessary
        if img.height > 2550 or img.width > 3300:
            output_size = (2550, 3300)
            img.thumbnail(output_size)

        # Save as Coloring Page
        img.save(self.Coloring_Page.path)

    def get_absolute_url(self):
        return reverse('edit-page', kwargs={'pk': self.id})
