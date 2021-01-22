from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from booktest.models import BookInfo


class ModelView(View):
    def post(self,request):
        # 增加
        # book = BookInfo()
        # book.btitle = '颈椎病修复术'
        # book.bpub_date = '2008-01-01'
        # book.save()
        #
        # BookInfo.objects.create(
        #     btitle='腰椎病修复术',
        #     bpub_date = '2020-01-01'
        # )

        return HttpResponse('ok')


# BookInfo.objects.filter(属性名字__运算符=值)
# 查询编号为1的图书。(id=1) -- (id__exact=1)
# 查询书名包含'传'的图书。(btitle__contains='传')
# 查询书名以'部'结尾的图书(btitle__endswith='部')
# 查询书名不为空的图书。(btitle__isnull=False)
# 查询编号为1或3或5的图书 (id__in=[1,3,5])
# 查询编号大于3的图书 gt lt gte lte (id__gt=3)

# 查询阅读量大于等于评论量的图书。
# 查询阅读量大于2倍评论量的图书。

# 查询阅读量大于20，并且编号小于3的图书
# BookInfo.objects.filter(Q(bread__gt = 20) & Q(id__lt=3))

# 查询阅读量大于20，或编号小于3的图书
# BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt = 3))

# 查询阅读量不等于3的图书--- ~
# BookInfo.objects.filter(~Q(id=3))

# 查询 所有图书的平均阅读量
# BookInfo.objects.aggregate(Avg('bread'))


# 查询 Id=3这本书的所有英雄



