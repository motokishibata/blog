# Generated by Django 2.1 on 2019-05-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_auto_20190516_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]