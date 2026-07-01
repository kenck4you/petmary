from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_pet/', views.create_pet, name='create_pet'),
    path('pet/<int:pet_id>/', views.pet, name='pet')
]