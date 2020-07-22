from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/<str:type>', views.upload, name='upload'),
]
