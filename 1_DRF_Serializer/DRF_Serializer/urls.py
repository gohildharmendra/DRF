from django.contrib import admin
from django.urls import path, include
from Ex_serializer import views



urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',views.student_list),
    path('stuinfo/',views.student_list),
    path('stuinfo/<int:pk>',views.student_details),    
]
