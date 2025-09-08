from django.db import models # type: ignore # type: ignore

# Create your models here.
from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField(default=0)
#     image = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     created_at = models.DateField()



from django.db import models

class Product(models.Model):
    # Basic fields
    name = models.CharField(max_length=200, verbose_name="Art Title")
    description = models.TextField(help_text="Write a short description of the Art")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # Media field
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # Date and time fields
    published_date = models.DateField(null=True, blank=True)
    available_from = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Choices field
    GENRE_CHOICES = [
        ("Status", "Status"),
        ("Paint", "Paint"),
    ]
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default="Paint")

    # Inner Meta class
    class Meta:
        ordering = ['-created_at']  # latest books first
        verbose_name = "Art"
        verbose_name_plural = "Art"

    def __str__(self):
        return self.name