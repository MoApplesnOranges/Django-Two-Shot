from receipts.models import Receipt
from django.forms import ModelForm
from django import forms


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]
