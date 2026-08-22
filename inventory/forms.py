from django import forms

from .models import WarehouseProduct


class WarehouseProductForm(forms.ModelForm):
    class Meta:
        model = WarehouseProduct
        fields = ["sku", "name", "quantity"]