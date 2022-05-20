from django.shortcuts import render
from .models import Place,Place1
# Create your views here.


def demo(request):
    obj=Place.objects.all()
    obj1=Place1.objects.all()
    return render(request,"index.html",{'result':obj,'result1': obj1})



