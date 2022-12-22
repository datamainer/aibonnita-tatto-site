from django.db import models


class GalleryImg(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=64,
        unique=True,
    )

    image = models.ImageField(
        upload_to="gallery_images",
        blank=False,
    )

    def __str__(self):
        return self.name


class ScetchImg(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=64,
        unique=True,
    )

    image = models.ImageField(
        upload_to="gallery_images",
        blank=False,
    )

    def __str__(self):
        return self.name


