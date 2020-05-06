from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lastsms/', views.lastsms, name='lastsms')
]

