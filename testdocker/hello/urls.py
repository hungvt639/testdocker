from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('hello', views.hello.as_view(), name='hello'),
    path('sos', views.sos.as_view(), name='sos'),
    path('createsuperuser', views.create_superuser.as_view()),
    path('', views.xam_xi.as_view(), name='xam_xi')
]