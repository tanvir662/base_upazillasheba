from django.contrib import admin


from .models import Generalpeople
from .models import Complain

# Register your models here.


admin.site.register(Generalpeople)
admin.site.register(Complain)
