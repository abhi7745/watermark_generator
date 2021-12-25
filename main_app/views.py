# from django.db import reset_queries
# from django import http
# from watermark_generator import settings
from django.shortcuts import render,redirect


from PIL import Image,ImageDraw,ImageFont # it is for watermark gernerating purpose
import os

# import urllib.request

from main_app.models import *

# from django.http import HttpResponse, response


# Create your views here.

def index(request):
    
    # case 1
    # method post case start /////////////////////
    if request.method=='POST':
        user_watermark=request.POST.get('user_watermark')
        user_photo=request.FILES['user_photo']
        print(user_watermark)
        print(user_photo)


        if image_handler.objects.filter(watermark_name=user_watermark,user_image=user_photo).exists():

            return render(request,'index.html',{'checker':'Error.. Please refresh the window or go to image page '})
        else:
            temp_img=image_handler()
            temp_img.watermark_name=user_watermark
            temp_img.user_image=user_photo
            temp_img.save()

            abc=os.listdir('media/') # colleecting media folder all images and pass to the function add_watermark()
            print(abc)
            for x in abc:
                print(x)
                
            # add_watermark('media/user_image/img.jpg')
            add_watermark('media/'+x,user_watermark.capitalize())# calling add_watermark function

            return redirect(viewer)
            
    # method post case start //////////////////////////

    # case 2
    # /////////////////////////////////////////////////////////////

    # deleteing temporary data fom image_handler db
    myimagedb=image_handler.objects.all() # callimg all image_handler db for deleting
    print(myimagedb.count(),'the count')

    if myimagedb.count() > 0: # database checker

        #1 delete all user temporary value image from main media folder
        for image_remover in myimagedb: # this is for passing queryset value
            # print(myimagedb.count(),'the for loop count')

            if len(image_remover.user_image) > 0: # it will check the old image is not empty or not
                os.remove(image_remover.user_image.path)  #then delete the image

        print('main media folder deleted')

        #2 delete all user temporary database image
        myimagedb.delete()
        print('all user temporary database deleted') 

    # # delete all user temporary converted image from converted folder(media/converted/media)
    converded=os.listdir('media/converted/media/') #delete converted image
    for deleteimg in converded:
        print(deleteimg,'deleteimg')
        os.remove('media/converted/media/'+deleteimg)
        
    print('all converted images deleted ')
            
        # return redirect(index)
    # /////////////////////////////////////////////////////////////

    return render(request,'index.html')

def viewer(request):

    myimagedb=image_handler.objects.all()
    # counter=myimage.count()
    # print(counter)
    # for x in myimage:
    #     print(x.user_image)

    if myimagedb.count() == 0 :
        print('if')
        return redirect(index)
    
    else:
        print('else')

        converded=os.listdir('media/converted/media/')
        for converted_imagename in converded:
            print(converted_imagename)

        return render(request,'viewer.html',{'myimage':myimagedb,'imagename':converted_imagename})

# The main custom function for watermark generator
def add_watermark(image,usertext):  # 'image' variable holds 'media/image name' &  'usertext" holds user watermark from form
    
    img=Image.open(image).convert("RGBA") # opend a image from 'media/imagename.jpg' & convert to a rgba image (Assign the image from folder)
    txt=Image.new("RGBA",img.size,(255,255,255,0)) # create a new transparent(0) 'image' with the size of 'current image'

    # text="Abhijith KR"
    text=usertext  # passing watermark 'text' from the render function index
    font=ImageFont.truetype("arial.ttf",150)  # assign font 'name' and 'size'

    d = ImageDraw.Draw(txt) #creating a object for drawing the image(which image to draw- [we can draw on 'transparent' image] with 'user text') 

    # calculation for text
    width ,height = img.size
    textwidth , textheight = d.textsize(text,font)
    x = width/2 - textwidth/2
    y = height-textheight-300

    d.text((x,y), text , fill=(255,255,255,125), font=font)

    watermarked = Image.alpha_composite(img,txt)
    img_name = os.path.splitext(image)[0]
    watermarked.save('media/converted/'+ img_name + "_watermarked.png")


# def downloader(request,pk):
#     print(pk)
#     myimage_db=image_handler.objects.get(my_id=pk)

#     if len(myimage_db.user_image) > 0: # it will check the old image is not empty or not
#         os.remove(myimage_db.user_image.path)  #then delete the image

#     myimage_db.delete() # delete user temporary database image

#     converded=os.listdir('media/converted/media/') #delete converted image
#     for deleteimg in converded:
#         print(deleteimg,'deleteimg')
#         os.remove('media/converted/media/'+deleteimg)

    
#     return redirect(index)
    # return render(request,'downloader.html',{})


# def downloader(request,pk):
#     print(pk)
#     # file_path=os.path.join(settings.MEDIA_ROOT,path)
#     # if os.path.exists(file_path):
#     #     with open(file_path,'rb') as fh:
#     #         response=HttpResponse(fh.read(),content_type="application/adminupload")
#     #         response['content-Disposition']='inline;filename='+os.path.basename(file_path)
#     #         return response
#     # raise Http404


    

#     return render(request,'downloader.html',{})

# def index(request):

#     if request.method=='POST':
#         user_watermark=request.POST.get('user_watermark')
#         # user_photo=request.POST.get('user_photo')
#         print(user_watermark)
#         # print(user_photo)


        # userImg=request.FILES['user_photo']
        # print(userImg,'userImguuuuuuuuuuuuuuuuuuuuu')

       

        
    
        # add_watermark('img1.jpg',userImg)


        # img=Image.open(r"F:\Python Main\My Django Main\For Biodata\watermark_generator\img1.jpg").convert("RGBA")
        # txt=Image.new("RGBA",img.size,(255,255,255,0))

        # # text="Abhijith KR"
        # font=ImageFont.truetype("arial.ttf",75)

        # d = ImageDraw.Draw(txt)

        # width ,height = img.size
        # textwidth , textheight = d.textsize(user_watermark,font)
        # x = width/2 - textwidth
        # y = height-textwidth-300

        # d.user_watermark((x,y), user_watermark , fill=(255,255,255,125), font=font)

        # watermarked = Image.alpha_composite(img,txt)
        # img_name = os.path.splitext(userImg)[0]
        # watermarked.save('converted/'+ img_name + "_watermarked.png")


    # return render(request,'index.html')



# def add_watermark(image,abc):
#     print(abc)
#     urllib.request.urlretrieve(
#   'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
#    "gfg.png")
#     img=Image.open("gfg.png").convert("RGBA")
#     txt=Image.new("RGBA",img.size,(255,255,255,0))

#     # text="Abhijith KR"
#     # font=ImageFont.truetype("arial.ttf",75)

#     # d = ImageDraw.Draw(txt)

#     # width ,height = img.size
#     # textwidth , textheight = d.textsize(text,font)
#     # x = width/2 - textwidth
#     # y = height-textwidth-300

#     # d.text((x,y), text , fill=(255,255,255,125), font=font)

#     # watermarked = Image.alpha_composite(img,txt)
#     # img_name = os.path.splitext(image)[0]
#     # watermarked.save('converted/'+ img_name + "_watermarked.png")





