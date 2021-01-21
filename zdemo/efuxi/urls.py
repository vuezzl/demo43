from django.urls import path,include
from . import views

urlpatterns = [

    path('efuxi/<str:username>/', views.EfuxiView.as_view()),


]
