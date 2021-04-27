from django.contrib import admin

from Product.models import product
from Product.models import category


admin.site.register(product)
admin.site.register(category)
