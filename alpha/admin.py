# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group, User
from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ForeCastAdmin(admin.ModelAdmin):
    list_display = ['category', 'sub_category', 'user', 'heading']
    search_fields = ['category', 'sub_category', 'user']
    list_filter = ('category', 'sub_category',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


class BettingAdmin(admin.ModelAdmin):
    list_display = ['forecast', 'users', 'bet_for', 'bet_against']
    change_form_template = 'change_list.html'
    search_fields = ['users', 'forecast']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'txnid', 'order_date']
    search_fields = ['user']
    list_filter = ('user', 'amount', 'order_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ForeCast, ForeCastAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Betting, BettingAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.site_title = 'ForeCast Guru'
admin.site.site_header = 'ForeCast Guru'
admin.site.index_title= 'Dashboard'
