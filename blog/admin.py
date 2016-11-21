from django.contrib import admin
from blog import models

# Register your models here.

admin.AdminSite.site_header = 'Roddy 博客管理后台'
admin.AdminSite.site_title = 'My Blog'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc',)
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title',  'content', 'user', 'category', 'tag',)
        }),
        ('高级属性', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend','desc',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'content', 'user', 'article')

class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'callback_url','description', 'date_publish', 'index',)
    list_display_links = ('callback_url','title')
    list_editable = ('index',)


class AdAdmin(admin.ModelAdmin):
    list_display = ('title','description','callback_url','date_publish','index','image_url')
    list_editable = ('index','callback_url')
    list_display_links = ('title',)

admin.site.register(models.User)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Ad,AdAdmin)
admin.site.register(models.Links, LinksAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag)

