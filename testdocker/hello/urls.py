from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.hello.as_view(), name='hello'),
    path('sos', views.sos.as_view(), name='sos'),
    path('createsuperuser', views.create_superuser.as_view())
]