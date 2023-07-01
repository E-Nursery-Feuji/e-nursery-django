from django.urls import path
from . import views


urlpatterns = [
    path('images/',views.getAllImages),
    path('image/<int:id>/',views.getImageById),
     path('saveimage/', views.saveImage, name='save_image'),
    path('updateimage/',views.updateImage),
    path('deleteimage/<int:id>/',views.deleteImageById),

    path('types/',views.getAllTypes),
    path('type/<int:id>/',views.getTypeById),
    path('savetype/',views.saveType),
    path('updatetype/',views.updateType),
    path('deletetype/<int:id>/',views.deleteType),



    path('products/',views.getAllProducts),
    path('product/<int:id>/',views.getProductById),
    path('saveproduct/',views.saveProduct),
    path('updateproduct/',views.updateProduct),
    path('deleteproduct/<int:id>/',views.deleteProductById),


    path('blogs/',views.getAllBlogs),
    path('blog/<int:id>/',views.getBlogById),
    path('saveblog/',views.saveBlog),
    path('updateblog/',views.updateBlog),
    path('deleteblog/<int:id>/',views.deleteBlog),

]
