"""urls"""
from django.urls import path
from .views import  index, detail, create, create_item, delete_list, delete_item, update

app_name = 'polls'
urlpatterns = [
    path('', index, name="index"),
    path('<int:list_id>/', detail, name='list_detail'),
    path('create/', create, name='list_create'),
    path('<int:list_id>/delete', delete_list, name='list_del'),
    path('<int:list_id>/create', create_item, name='item_create'),
    path('<int:list_id>/<int:item_id>/delete', delete_item, name='item_del'),
    path('<int:list_id>/<int:item_id>/update', update, name='item_update')
]
