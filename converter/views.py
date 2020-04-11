from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, UpdateView

from converter.forms import UploadImageForm, UpdateColoringPageForm
from gallery.models import Image


@login_required
def UploadImage(request):
    if request.method == 'POST':
        upload_img_form = UploadImageForm(request.POST, request.FILES)
        if upload_img_form.is_valid():
            image = upload_img_form.save(commit=False)
            image.owner = request.user
            image.Coloring_Page = upload_img_form.cleaned_data.get("Original_Image")
            image.save()
            messages.success(request, f'Image has been uploaded!')
            return redirect('gallery-home')
    else:
        upload_img_form = UploadImageForm()

    context = {
        'upload_img_form': upload_img_form
    }
    return render(request, "converter/upload_form.html", context)


def EditImage(request, pk):
    if request.method == 'POST':
        update_form = UpdateColoringPageForm(request.POST)
        if update_form.is_valid():
            image = update_form.save()
            messages.success(request, f'Image has been edited!')
            return redirect('page-detail', pk)
    else:
        upload_img_form = UploadImageForm()

    context = {
        'upload_img_form': upload_img_form
    }
    return render(request, "converter/upload_form.html", context)


class UpdateColoringPageView(LoginRequiredMixin, UpdateView):
    model = Image
    fields = ['sigma']
