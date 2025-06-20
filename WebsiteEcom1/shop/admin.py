from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header = "Ecommerce"
admin.site.site_title = "admin"
admin.site.index_title = "manage Ecom site"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','category','image')
    search_fields = ('title',)
    list_editable = ('price',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)