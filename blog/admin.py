from django.contrib import admin
from blog.models import Post, Category, SubCategory

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SubCategory)