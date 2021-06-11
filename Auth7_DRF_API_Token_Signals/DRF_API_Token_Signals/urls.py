from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
#Creating Router object
router = DefaultRouter()
#Register StudentViewSet with router
router.register('student_api', views.StudentModalViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #Generate AuthToken
    
      
]