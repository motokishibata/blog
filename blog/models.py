from django.db import models


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
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.title
