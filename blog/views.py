#:coding:utf8
from django.shortcuts import render
from django.conf import settings
from blog.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def global_setting(request):
    return{'SITE_NAME':"普拉多VX",
            'SITE_DESC':"开发路遥远，壮士需努力",
            'SITE_TENCENT':"923401910",
            'SITE_BLOG':"http://www.roddypy.com",}

def index(request):
    if request.method == 'GET':
        #分类数据
        category_list=Category.objects.all()
        #广告轮播数据
        Ad_list = Ad.objects.all()
        #文章列表
        Article_list = Article.objects.all()

        archive_list = Article.objects.distinct_date()


        paginator = Paginator(Article_list,10)
        try:
            page = int(request.GET.get('page', 1))
            Article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            Article_list = paginator.page(1)

    return render(request, 'index.html', locals())

def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        # 分类数据
        category_list = Category.objects.all()
        # 广告轮播数据
        Ad_list = Ad.objects.all()
        # 文章列表
        Article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        archive_list = Article.objects.distinct_date()

        paginator = Paginator(Article_list, 10)
        try:
            page = int(request.GET.get('page', 1))
            Article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            Article_list = paginator.page(1)
    except Exception as e:
        print(e)
    return render(request,'archive.html',locals())
