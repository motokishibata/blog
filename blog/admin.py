from django.contrib import admin
from blog.models import Post, Category, SubCategory, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Comment)