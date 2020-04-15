from django.urls import path
from .views import policeview

urlpatterns = [
    path('policeview/',policeview,name='policeview'),
]