from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user','name','locality','city','zipcode','state')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','selling_price','discounted_price','brand','category','product_image')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','product','quantity')

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id','customer','product','quantity','ordered_date','status')

