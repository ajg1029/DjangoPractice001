# Generated by Django 3.2.7 on 2023-05-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='images',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]