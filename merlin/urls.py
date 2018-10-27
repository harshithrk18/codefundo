from django.urls import path
from merlin import views

app_name = 'merlin'

urlpatterns = [
    path('register/', views.register,name='register'),
    path('user_login/', views.user_login, name='user_login'),

]