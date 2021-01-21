from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.http import HttpResponse, JsonResponse


class ResponseView(View):
    def get(self,request):
        # 响应对象的属性
        # response = HttpResponse()
        # response.content = 'content'
        #
        #
        #
        # return response
        # data_dict = {
        #     'city':'shanghai',
        #     'subject': 'python'
        # }
        # return JsonResponse(data_dict)
        # 响应对象的参数
        # content = '响应对象的参数'
        # status = 200
        # content_type = 'text/html'
        # return HttpResponse(content=content,status=status,content_type=content_type)


        return redirect('http://www.baidu.com')