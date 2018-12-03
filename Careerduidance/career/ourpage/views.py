from django.shortcuts import render

# Create your views here.
def ourpage1(request):
    return render(request,'ourpage/ourpage1.html')
