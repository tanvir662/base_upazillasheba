from django.contrib import admin

# Register your models here.
from assigncomplain.models import AssignComplainPolice, AssignComplainUno, AssignComplainChairman

admin.site.register(AssignComplainPolice)
admin.site.register(AssignComplainChairman)
admin.site.register(AssignComplainUno)