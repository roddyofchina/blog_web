from django.shortcuts import render
from django.conf import settings


def global_setting(request):
    return{'SITE_NAME':"普拉多VX",
            'SITE_DESC':"开发路遥远，壮士需努力",
            'SITE_TENCENT':"923401910",
            'SITE_BLOG':"http://www.roddypy.com",}

def index(request):

    return render(request, 'index.html', locals())
