from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Category_Field)
admin.site.register(Product)
admin.site.register(Product_Image)