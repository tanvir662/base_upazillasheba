from django.shortcuts import render, HttpResponse, redirect

from police.models import Police
from police.views import  policeview
from chairman.models import Chairman
from chairman.views import chairmanview
from uno.models import Uno
from uno.views import unoview


def login(request):

    if request.method == "POST":
        userType = request.POST.get("userType")

        if userType == "Police":
            username = request.POST.get("username")
            password = request.POST.get("password")
            police = Police.objects.all().filter(username=username, password=password)
            for pol in police:
                print(pol.policeId)
                request.session['id'] = pol.policeId
                request.session['userType']="Police"

            if police:
                return redirect(policeview)
            else:
                return redirect(login)

        elif userType == "Chairman":
            username = request.POST.get("username")
            password = request.POST.get("password")
            chairman = Chairman.objects.all().filter(username=username,password=password)
            for cha in chairman:
                print (cha.chairmanId)
                request.session['id'] = cha.chairmanId
                request.session['userType']="Chairman"

            if chairman:
                return redirect(chairmanview)
            else:
                return redirect(login)
        elif userType == "UNO":
            username = request.POST.get("username")
            password = request.POST.get("password")
            uno = Uno.objects.all().filter(username=username,password=password)
            for un in uno:
                print (un.unoId)
                request.session['id'] = un.unoId
                request.session['userType']="Uno"

            if uno:
                return redirect(unoview)
            else:
                return redirect(login)

    return render(request, "Account/login.html", {})
