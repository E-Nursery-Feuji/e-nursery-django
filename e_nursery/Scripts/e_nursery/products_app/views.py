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
from rest_framework import viewsets
from .models import Image
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def demo(request):
    return HttpResponse('product app')

@csrf_exempt    
def getAllImages(request):
        log.info("GET method")
        images=Image.objects.all()
        serialized_images = []

        for image in images:
                image_serializer = ImageSerializer(image, context={'request': request})
                serialized_images.append(image_serializer.data)

        log.info("getting all images")
        return JsonResponse(serialized_images,safe=False)   
 
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
class SaveImage(viewsets.ModelViewSet):
       log.info("Starts")
       queryset=Image.objects.all()
       serializer_class=ImageSerializer
       log.info("Serialized")

       def post(self,request):
              log.info("Enter in function")
              log.info(request.data)
              log.info(request.FILES)
              image=request.data['image']
              return HttpResponse("Submit")

# @csrf_exempt       
# def saveImage(self,request):
#         log.info("saveImage : starts")
#         log.info(request.FILES)
#         if 'image' in request.FILES: #check the image is present as file or not
#                 log.info("Image Present in the request")
#                 return self.create(request)
#                 # image_file = request.FILES['image'] #get the image from the request
#                 # log.info("Image is reading...")
#                 # image_data = image_file.read() #get the image data from the image
#                 # log.info("Image reading Completed")
#                 # image = Image() #create the object of the image model
#                 # # log.info(image_data)
#                 # image.image_data = image_data #assign the image data in the object
#                 # log.info(image)
#                 # image.save() #save the image in database
#                 # log.info("Image saved")
#                 # serialized_image = serialize('json', [image])
#                 # return JsonResponse(serialized_image, safe=False)
#                 # return HttpResponse(image) #response if image save succesfuuly
#         log.info("Image is not present in request")
#         return HttpResponse("Invalid request.") #reponse if image is not there in request

# @csrf_exempt 
# def saveImage(request):
#         if request.data:
               

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
                return JsonResponse(product_serializer.data,safe=False)
        else:
                log.info("save product data ia not valid change")
        return JsonResponse("not added",safe=False)
        
       
@csrf_exempt    
def updateProduct(request):
        product_data=JSONParser().parse(request)       
        product=Product.objects.get(id=product_data['id'])
        log.info(product_data)
        product_serializer=ProductSerializer(product,data=product_data)
        log.info("update product==")
        log.info(product_serializer)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data,safe=False)
        return JsonResponse("not updated",safe=False)
    
@csrf_exempt    
def deleteProductById(request,id):
        product = Product.objects.get(id=id)
        image = Image.objects.get(id=product.image_id)
        products_serializer=ProductSerializer(product)
        product.delete()  
        image.delete()  
        return JsonResponse(products_serializer.data, safe=False)

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


@api_view(['PATCH'])
def status(request, id):
    log.info("Enter into insert Schedule")
    try:
        schedule = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)

    # Assign the field value "InActive" to the desired field

    if (schedule.status == "Active"):
        schedule.status = "InActive"
    elif (schedule.status == "InActive"):
        schedule.status = "Active"
    else:
        schedule.status = "InActive"

                        
    try:                   # Save the updated Schedule object
        schedule.save()    # Return the serialized data in the response
        serializer = BlogSerializer(schedule)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)