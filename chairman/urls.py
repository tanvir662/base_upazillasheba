from django.urls import path
from .views import chairmanview

urlpatterns = [
    path('chairmanview/',chairmanview,name='chairmanview'),
]