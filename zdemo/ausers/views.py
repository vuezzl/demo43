from django.http import HttpResponse
from django.shortcuts import render





def register(request):
    return HttpResponse('注册接口')
def index(request):

    return HttpResponse ('helloworld')


