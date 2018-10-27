# from django.urls import path
from django.conf.urls import url,include
from merlin import views

app_name = 'merlin'


urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
