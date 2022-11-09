from django.contrib import admin
from django.urls import path
from hashing_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hash/<str:hash>', views.hash, name='hash'),
]
