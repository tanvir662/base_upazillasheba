from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',views.home,name='gereralpeople_from'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)