# Generated by Django 3.1.1 on 2021-09-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210920_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_handler',
            name='user_image',
            field=models.ImageField(upload_to=None),
        ),
    ]