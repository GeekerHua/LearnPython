# coding=utf-8
from django.contrib import admin
from .models import *
# Register your models here.

# class AreaInfoInline(admin.StackedInline):
#     model = AreaInfo
#     extra = 2


class AreaInfoInlineTable(admin.TabularInline):
    model = AreaInfo
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    # 列表页选项
    list_per_page = 10
    actions_on_bottom = True
    list_display = ['id', 'atitle', 'aParent', 'title']
    list_filter = ['aParent']
    search_fields = ['atitle', 'id']
    # 编辑页选项
    fieldsets = (
        ('基本', {'fields': ('atitle',)}),
        ('高级', {'fields': ('aParent',)})
    )
    inlines = [AreaInfoInlineTable]


admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(picTest)
