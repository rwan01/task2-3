from django.db import models

# Create your models here.


class Art(models.Model):
    title = models.CharField(max_length=100)          # name of the artwork
    artist = models.CharField(max_length=100)         # artist name
    description = models.TextField(blank=True)        # optional longer text
    created_year = models.PositiveIntegerField()      # year the art was created
    medium = models.CharField(max_length=100)         # e.g. Oil on canvas, Sculpture
    dimensions = models.CharField(max_length=100, blank=True)  # e.g. "24 x 36 in"
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # optional
    image = models.ImageField(upload_to='art_images/', blank=True, null=True)  # store images
    created_at = models.DateTimeField(auto_now_add=True)  