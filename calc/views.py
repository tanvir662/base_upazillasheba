from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
# Create your views here.
from calc.models import Generalpeople, Complain


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method=='POST':

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        district = request.POST.get("district")
        upozilla = request.POST.get("upozilla")
        union = request.POST.get("union")
        village =request.POST.get("village")

        addMed = Generalpeople(name=name,phone=phone,district=district, upozilla=upozilla, union=union,village=village)
        addMed.save()
        catagory = request.POST.get("catagory")
        complain=request.POST.get("complain")
        file=request.POST.get("file")
        addMed1 = Complain(catagory=catagory,complain=complain,file=file,gp_id=addMed)
        addMed1.save()
        return render(request, 'index.html')


