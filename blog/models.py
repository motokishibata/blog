from django.db import models
import re

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    current_category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="image", null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def preview_content(self):
        delete_tag_pattern = r'<.+?>'
        deleted_tag_content = re.sub(delete_tag_pattern, '', self.content)
        make_content = ''
        if len(deleted_tag_content) > 50:
            make_content = deleted_tag_content[0:50]
        else:
            make_content = deleted_tag_content + '...'
        return make_content
