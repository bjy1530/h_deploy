
from django.contrib import admin
from django.urls import path
import myblog.views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myblog.views.home,name='home'),
]
