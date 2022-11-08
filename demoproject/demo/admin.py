from django.contrib import admin
from demo.forms import OrderForm
from demo.models import *


# Register your models here.
class ProductInOrder(admin.TabularInline):
    model = ProductInOrder


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_filter = ('status',)
    list_display = ('date', 'user', 'count_product')
    fields = ['status', 'rejection_reason']
    inlines = (ProductInOrder,)


admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Order, OrderAdmin)
