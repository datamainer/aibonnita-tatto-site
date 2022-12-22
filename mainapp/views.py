from django.shortcuts import render

# Create your views here.
from mainapp.models import GalleryImg, ScetchImg


def main(request):
    gallery_img = GalleryImg.objects.all()
    scetch_img = ScetchImg.objects.all()

    context = {
        'gallery_img': gallery_img,
        'scetch_img': scetch_img,
    }

    return render(request, 'mainapp/index.html', context=context)

