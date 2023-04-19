from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Receipt


# Create your views here.
def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {"receipts": receipts}
    return render(request, "receipts/list.html", context)
