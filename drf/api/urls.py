from django.urls import path
from . import views

urlpatterns = [
    path('sample/',views.getData),
    path('add/',views.additem),
]
