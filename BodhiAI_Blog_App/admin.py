from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Category,Topic,Blog,Comment
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(Comment)