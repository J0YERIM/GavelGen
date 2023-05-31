from django.contrib import admin
from .models import Product, Comment, Tag, Report, Heart

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Report)
admin.site.register(Heart)
