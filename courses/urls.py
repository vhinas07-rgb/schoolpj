from django.urls import path
from . import views 

urlpatterns =[
    path('', views.home_view,name='home'),
    path('<int:pid>/',views.detail_view,name='details')
]