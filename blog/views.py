#:coding:utf8
from django.shortcuts import render
from django.conf import settings
from blog.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def global_setting(request):
    # 分类数据
    category_list = Category.objects.all()
    # 广告轮播数据
    Ad_list = Ad.objects.all()

    archive_list = Article.objects.distinct_date()

    return{'SITE_NAME':"普拉多VX",
            'SITE_DESC':"开发路遥远，壮士需努力",
            'SITE_TENCENT':"923401910",
            'SITE_BLOG':"http://www.roddypy.com",
            'category_list':category_list,
            'Ad_list':Ad_list,
            'archive_list':archive_list}

def index(request):
    if request.method == 'GET':
        #文章列表
        Article_list = Article.objects.all()
        Article_list = getPage(request,Article_list)
    return render(request, 'index.html', locals())

def archive(request):
    try:
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        # 文章列表
        Article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        Article_list=getPage(request,Article_list)
    except Exception as e:
        print(e)
    return render(request,'archive.html',locals())

def getPage(request,Article_list):
    paginator = Paginator(Article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        Article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        Article_list = paginator.page(1)
    return Article_list




