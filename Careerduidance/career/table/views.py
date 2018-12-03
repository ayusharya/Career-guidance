from django.shortcuts import render
from.models import *

# Create your views here.
def table11(request):
    table=Table.objects.all().order_by()
#for order     table=Table.objects.all().order_by('date')
    return render(request,'table/table11.html', { 'table': table })

def table22(request):
    table=Table2.objects.all()
#for order     table=Table.objects.all().order_by('date')
    return render(request,'table/table22.html',{'table':table})


def table33(request):
    table=Table3.objects.all()
#for order     table=Table.objects.all().order_by('date')
    return render(request,'table/table33.html',{ 'table': table})
