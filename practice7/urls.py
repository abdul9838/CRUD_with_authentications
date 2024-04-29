from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

routes = DefaultRouter()
routes.register('',views.StudentApi,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes.urls)),
    path('auth/', include('rest_framework.urls')),
]
