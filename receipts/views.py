from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {"receipts": Receipt.objects.filter(purchaser=request.user)}
    return render(request, "receipts/list.html", context)
