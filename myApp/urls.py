from django.urls import path
from myApp.views import home, read, delItem, upItem

urlpatterns = [
   
    path('',home ),
     path('table/',read, name="table"),
     path('Delete/<int:pk>',delItem, name="de"),
     path('Update/<int:pk>',upItem, name="up"),
]