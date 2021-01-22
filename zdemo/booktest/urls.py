from django.urls import path,include
from . import views

urlpatterns = [

    path('model/', views.ModelView.as_view()),


]
