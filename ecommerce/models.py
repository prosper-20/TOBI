from django.db import models

CATEGORY_CHOICES = (
    ("F", "Fashion"),
    ("E", "Electronics"),
    ("B", "Bags"),
    ("C", "Clothes")
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="product_images", default="product.jpg")


    def __str__(self):
        return self.name
