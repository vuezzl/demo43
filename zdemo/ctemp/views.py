from django.shortcuts import render

# Create your views here.
from django.views import View
class TempView(View):
    def get(self,request):
        return render(request,'index.html',{'username':'张三'})
