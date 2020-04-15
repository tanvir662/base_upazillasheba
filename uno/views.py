from django.shortcuts import render
from assigncomplain.models import AssignComplainUno
# Create your views here.
from uno.models import Uno


def unoview(request):

      uID = request.session.get('id')
      uno = Uno.objects.get(unoId=uID)
      print(uno)
      assignComplainUnos = AssignComplainUno.objects.all().filter(uno=uno)

      print(assignComplainUnos)
      if request.POST.get('assign'):
            status = request.POST.get('status')
            date = request.POST.get('date')
            time = request.POST.get('time')
            assignComId = int(request.POST.get('assignComId'))
            for assignComplainU in assignComplainUnos:
                  if assignComplainU .complainId==assignComId:
                        assignComplainU .setmeetingdate=date
                        assignComplainU .setmeetingtime = time
                        assignComplainU .status = status
                        assignComplainU .save()

      return render(request, "uno_complain_list.html", {'assignComplainUnos': assignComplainUnos})

