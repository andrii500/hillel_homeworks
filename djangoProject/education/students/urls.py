from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('generate-student/', views.get_generate_student, name='generate-student'),
    path('generate-students/', views.get_generate_students, name='generate-students')
]
