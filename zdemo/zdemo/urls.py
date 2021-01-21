"""zdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,register_converter
from converters import MobileConverter

from ausers.views import index
register_converter(MobileConverter,'mobile')


urlpatterns = [
    path('admin/', admin.site.urls),
    # 路由找到函数
    path('login/',index),
    # 路由找自路由找函数
    path('register/', include('ausers.urls')),
    path('', include('ctest.urls')),
    path('', include('dresponse.urls')),
    path('', include('efuxi.urls')),

]
