from django.db import models


class WarehouseProduct(models.Model):
    """Simulates products stored in the warehouse system."""

    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.quantity}"


class InventoryItem(models.Model):
    """The inventory service's locally cached stock."""

    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def in_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f"{self.sku} - {self.quantity}"