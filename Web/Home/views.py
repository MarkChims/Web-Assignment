from django.shortcuts import render
from .models import Goods


# Create your views here.
def homepage(request):
    goods = Goods.objects.all()
    return render(request, "Home/Home.html", {"goods": goods})
