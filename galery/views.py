from django.shortcuts import render

from galery.models import GalleryPage


# Create your views here.
def galery(request):
    gallery_img = GalleryPage.objects.all()

    context = {
        'gallery_img': gallery_img,
    }

    return render(request, 'galery/gallery.html', context=context)
