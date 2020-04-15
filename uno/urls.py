from django.urls import path
from .views import unoview

urlpatterns = [
    path('unoview/',unoview,name='unoview'),
]