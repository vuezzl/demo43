from django.urls import path,include
from . import views

urlpatterns = [

    path('dresponse/', views.ResponseView.as_view()),


]
