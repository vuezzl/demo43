from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

class EfuxiView(View):
    def post(self,request,username):
        print('路径参数:',username),
        print('请求提:',request.POST.get('password'))
        print('查询参数:',request.GET.get('age'))
        print('请求头:',request.META.get('HTTP_GENDER'))

        return JsonResponse({"name":'参数四种的作业'})


