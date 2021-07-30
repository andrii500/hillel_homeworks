from django.urls import path
from . import views


urlpatterns = [
    path('teachers/', views.get_teachers, name='teachers'),
]
