from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *
from .serializer import BlogSerializer
import logging as log
from django.core.serializers import serialize
from django.http import JsonResponse
# Create your views here.

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def demo(request):
    return HttpResponse('product app')

@csrf_exempt    
def getAllImages(request):
        log.info("GET method")
        images=Image.objects.all()
        images_serializer=ImageSerializer(images,many=True)
        log.info("getting all images")
        return JsonResponse(images_serializer.data,safe=False)   
 
@csrf_exempt 
def getImageById(request,id):
        image=Image.objects.get(id=id)
        log.info("getting image by")
        images_serializer=ImageSerializer(image)
        return JsonResponse(images_serializer.data,safe=False) 
   
@csrf_exempt 
def deleteImageById(request,id):
     image=Image.objects.get(id=id)
     image.delete()
     return JsonResponse("deleted successfully",safe=False)

#for save the image
@csrf_exempt       
def saveImage(request):
        log.info("saveImage : starts")
        if 'image' in request.FILES: #check the image is present as file or not
                log.info("Image Present in the request")
                image_file = request.FILES['image'] #get the image from the request
                log.info("Image is reading...")
                image_data = image_file.read() #get the image data from the image
                log.info("Image reading Completed")
                image = Image() #create the object of the image model
                image.image_data = image_data #assign the image data in the object
                image.save() #save the image in database
                log.info("Image saved")
                serialized_image = serialize('json', [image])
                return JsonResponse(serialized_image, safe=False)
                # return HttpResponse(image) #response if image save succesfuuly
        log.info("Image is not present in request")
        return HttpResponse("Invalid request.") #reponse if image is not there in request


@csrf_exempt 
def updateImage(request):
    image_data=JSONParser().parse(request)
    image=Image.objects.get(id=image_data['id'])
    image_serializer=ImageSerializer(image,data=image_data)
    if image_serializer.is_valid():
            image_serializer.save()
            return JsonResponse("UPDATED successfully...",safe=False)
    return JsonResponse("failed to save..",safe=False)


@csrf_exempt
def getAllTypes(request):
     types=Type.objects.all()
     types_serializer=TypeSerializer(types,many=True)
     return JsonResponse(types_serializer.data,safe=False)    

def getTypeById(request,id):
     type=Type.objects.get(id=id)
     types_serializer=TypeSerializer(type)
     return JsonResponse(types_serializer.data,safe=False)    


@csrf_exempt 
def deleteType(request,id):
      type=Type.objects.get(id=id)
      type.delete()
      return JsonResponse("deleted successfully",safe=False)
@csrf_exempt 
def saveType(request):
        type_data = JSONParser().parse(request)
        type_serializer=TypeSerializer(data=type_data)
        if type_serializer.is_valid():
            type_serializer.save()
            return JsonResponse("Saved successfully...",safe=False)
        return JsonResponse("failed to save...",safe=False)

@csrf_exempt 
def updateType(request):   
     type_data=JSONParser().parse(request)
     type=Type.objects.get(id=type_data['id'])
     type_serializer=TypeSerializer(type,data=type_data)
     if type_serializer.is_valid():
            type_serializer.save()
            return JsonResponse("UPDATED successfully...",safe=False)
     return JsonResponse("failed to save..",safe=False)
    

@csrf_exempt 
def getAllProducts(request):
      products=Product.objects.all()
      products_serializer=ProductSerializer(products,many=True)
      return JsonResponse(products_serializer.data,safe=False) 
@csrf_exempt    
def getProductById(request,id):
      product=Product.objects.get(id=id)
      products_serializer=ProductSerializer(product)
      return JsonResponse(products_serializer.data,safe=False) 
@csrf_exempt 
def  saveProduct(request):   
        product_data = JSONParser().parse(request)
        product_serializer=ProductSerializer(data=product_data)
        log.info("save product is executed")
        if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse("product added",safe=False)
        # else:
        #         log.info("save product data ia not valid change")
        return JsonResponse("not added",safe=False)
        
       
@csrf_exempt    
def updateProduct(request):
        product_data=JSONParser().parse(request)       
        product=Product.objects.get(id=product_data['id'])
        product_serializer=ProductSerializer(product,data=product_data)
        log.info("update product==")
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("product updated",safe=False)
        return JsonResponse("not updated",safe=False)
    
@csrf_exempt    
def deleteProductById(request,id):
        product = Product.objects.get(id=id)
        image = product.image 
        product.delete()  
        image.delete()  
        return JsonResponse("Deleted", safe=False)
@csrf_exempt 
def getAllBlogs(request):
        log.info("GET method")
        blogs=Blog.objects.all()
        blogs_serializer=BlogSerializer(blogs,many=True)
        log.info("getting all blogs")
        return JsonResponse(blogs_serializer.data,safe=False) 



@csrf_exempt
def getBlogById(request,id):
            blog=Blog.objects.get(id=id)
            log.info("getting blog by id ")
            blogs_serializer=BlogSerializer(blog)
 
            return JsonResponse(blogs_serializer.data,safe=False) 
@csrf_exempt
def saveBlog(request): 
        blog_data = JSONParser().parse(request)
        blog_serializer=BlogSerializer(data=blog_data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse("Saved successfully...",safe=False)
        return JsonResponse(blog_serializer.error_messages,safe=False)
@csrf_exempt
def updateBlog(request):
        blog_data=JSONParser().parse(request)
        blog=Blog.objects.get(id=blog_data['id'])
        blog_serializer=BlogSerializer(blog,data=blog_data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse("UPDATED successfully...",safe=False)
        return JsonResponse("failed to update..",safe=False)

@csrf_exempt
def deleteBlog(request, id):
        blog=Blog.objects.get(id=id)
        image = blog.image 
        blog.delete()  
        image.delete() 
        return JsonResponse("deleted successfully",safe=False)
