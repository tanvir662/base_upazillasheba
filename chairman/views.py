from django.shortcuts import render
from assigncomplain.models import AssignComplainChairman
# Create your views here.
from chairman.models import Chairman


def chairmanview(request):

      chairID = request.session.get('id')
      chairman = Chairman.objects.get(chairmanId=chairID)
      print(chairman)
      assignComplainChairmans = AssignComplainChairman.objects.all().filter(chairman=chairman)

      print(assignComplainChairmans)
      if request.POST.get('assign'):
            status = request.POST.get('status')
            date = request.POST.get('date')
            time = request.POST.get('time')
            assignComId = int(request.POST.get('assignComId'))
            for assignComplainChair in assignComplainChairmans:
                  if assignComplainChair.complainId==assignComId:
                        assignComplainChair.setmeetingdate=date
                        assignComplainChair.setmeetingtime = time
                        assignComplainChair.status = status
                        assignComplainChair.save()

      return render(request, "chairman_complain_list.html", {'assignComplainChairmans': assignComplainChairmans})

