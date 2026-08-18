from django.db import models

# Create your models here.
class InventoryItem(models.Model):
     sku = models.CharField(max_length=100, unique=True)
     name = models.CharField(max_length=200)
     quantity = models.PositiveIntegerField(default=0)
     updated_at = models.DateTimeField(auto_now=True)


     def in_stock(self):
        return self.quantity > 0

     def __str__(self):
        return f"{self.sku} - {self.quantity} in stock"