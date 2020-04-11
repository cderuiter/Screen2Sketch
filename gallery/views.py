from django.shortcuts import render, get_object_or_404
from .models import Image
from django.views.generic import ListView, DetailView
import io
from django.contrib.auth.models import User
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image as PilImage



class ColoringPageListView(ListView):
    model = Image
    template_name = 'gallery/home.html'
    context_object_name = 'image_list'
    paginate_by = 5


class UserColoringPageListView(ListView):
    model = Image
    template_name = 'gallery/user_coloring_pages.html'
    context_object_name = 'image_list'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(owner=user)


class ColoringPageDetailView(DetailView):
    model = Image
    context_object_name = 'image'


def DownloadColoringPageView(request, pk):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    # Get the Coloring Page by pk
    ColoringPage = Image.objects.filter(id=pk).first()

    # Open Coloring Page as Pillow Image
    img = PilImage.open(ColoringPage.Coloring_Page.path)
    img_width, img_height = img.size
    page_width, page_height = p._pagesize
    draw_width, draw_height = page_width, page_height
    aspect = img_height / float(img_width)

    # Print horizontally if necessary
    if img_width > img_height:
        page_width, page_height = page_height, page_width  # flip width/height
        draw_width, draw_height = draw_height, draw_width
        p.setPageSize((page_width, page_height))
        # Draw the Image on the Canvas
        p.drawInlineImage(img, x=(page_width - draw_width) / 2, y=(page_height - draw_height) / 2, width=draw_width,
                          height=draw_height, preserveAspectRatio=True)
    else:
        # Draw the Image on the Canvas
        p.drawInlineImage(img, x=0, y=0, width=draw_width, height=draw_height, preserveAspectRatio=True)

    # Save the Canvas
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='ColoringPage.pdf')
