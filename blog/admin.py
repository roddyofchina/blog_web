from django.contrib import admin
from blog import models

# Register your models here.

admin.AdminSite.site_header = 'Roddy 博客管理后台'
admin.AdminSite.site_title = 'My Blog'
admin.site.register(models.User)

