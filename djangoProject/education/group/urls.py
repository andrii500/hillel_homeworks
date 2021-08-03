from django.urls import path

from . import views


urlpatterns = [
    path('group/', views.get_group, name='group'),
]
