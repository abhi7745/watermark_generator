from django.db import models

import os

# Create your models here.

# def my_fun():
#     abc=os.listdir('media/')
#     # print(abc[0])
#     for x in abc:
#         os.rename(x,'edited.jpg')



class image_handler(models.Model):
    my_id=models.AutoField(primary_key=True)
    watermark_name=models.CharField(max_length=50)
    user_image=models.ImageField(upload_to="")
    