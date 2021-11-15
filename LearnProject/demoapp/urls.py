from django.conf.urls import url
from demoapp import views

app_name = 'demoapp'

urlpatterns=[
    url('index/', views.index, name = 'index'),
    url('register/', views.register, name='register'),
    url('login/', views.u_login, name='login'),
]
