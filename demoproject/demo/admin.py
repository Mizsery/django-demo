from django.contrib import admin

from demo.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(ProductInOrder)
admin.site.register(Cart)