# Generated by Django 2.2.4 on 2019-09-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
