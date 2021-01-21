from django.urls import path,include
from . import views

urlpatterns = [

    path('register/', views.RegisterView.as_view()),
    # 路径传参
    path('url_param/<int:age>/<mobile:mobile>', views.RegisterView.as_view()),

    path('path_param/', views.PathView.as_view()),

]
