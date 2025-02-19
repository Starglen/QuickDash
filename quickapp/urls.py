
from django.contrib import admin
from django.urls import path
from quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('gallery/', views.gallery,name='gallery'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),

]
