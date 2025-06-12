from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    producer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField()
    category = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name