# Generated by Django 3.1.1 on 2021-09-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210920_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_handler',
            name='user_image',
            field=models.ImageField(upload_to='user_image'),
        ),
    ]
