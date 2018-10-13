from django.shortcuts import render
from finance.models import StockIndexSnapShot


# Create your views here.

def index(request):
    # stock_index_snapshot = StockIndexSnapShot.objects.last()

    return render(request, 'finance/index.html')
