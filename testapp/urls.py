from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name="logout"),
    path('whatsapp/', views.whatsapp_redirect, name='whatsapp'),
    path('whatsapp_image/', views.whatsapp_redirect_with_image, name='whatsapp_image'),
]
