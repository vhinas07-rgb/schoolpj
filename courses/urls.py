from django.urls import path
from . import views 

urlpatterns =[
    path('', views.home_view,name='home'),
    path('<int:pid>/',views.detail_view,name='details'),
    path('form/', views.course_form_view, name='course_form'),
    path('<int:pid>/edit/', views.course_form_view, name='course_edit'),
    path('<int:pid>/delete/', views.delete_view, name='delete'),
]