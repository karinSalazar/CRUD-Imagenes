from django.urls import path

from .views import list_autos, create_autos, update_autos, delete_autos


urlpatterns = [
    path('', list_autos, name='list_autos'),
    path('new', create_autos, name='create_autos'),
    path('update/<int:id>/', update_autos, name='update_autos'),
    path('delete/<int:id>/', delete_autos, name='delete_autos'),
]
