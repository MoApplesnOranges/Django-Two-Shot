from receipts.models import Receipt, ExpenseCategory, Account
from django.forms import ModelForm
from django import forms


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "number"]
