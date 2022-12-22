from django.db import models


# Create your models here.
class GalleryPage(models.Model):
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
