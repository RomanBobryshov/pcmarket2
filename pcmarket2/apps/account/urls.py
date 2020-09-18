from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit')

]