import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class RegisterView(View):
    def get(self,request,age,mobile):
        # 查询参数传参
        params = request.GET
        name = params.get('name')

        print(name)
        # 路径传参
        print(age)
        print(mobile)



        return HttpResponse('返回注册')

    def post(self,request):
        # 请求体form表单传参
        data = request.POST
        age = data.get('age')
        print(age)
        # 请求提json非表单传参
        data_json  = json.loads(request.body.decode())
        print(data_json)


        return HttpResponse('实现注册逻辑')

class PathView(View):
    def get(self,request):
        headers_dict = request.META
        print('解析请求头的参数',headers_dict)
        print('解析请求头的参数',headers_dict['HTTP_NAME'])
        return HttpResponse('ok')