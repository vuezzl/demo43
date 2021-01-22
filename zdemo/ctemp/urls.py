from django.urls import path,include
from . import views

urlpatterns = [

    path('temp/', views.TempView.as_view()),


]
