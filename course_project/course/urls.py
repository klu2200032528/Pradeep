from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
