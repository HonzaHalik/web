from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name='index'),
path("krtek/", views.v1, name='krtek'),
]