from django.urls import path
from .views import createItem, index,detail,create,createItem,deleteList,deleteItem,update

app_name = 'polls'
urlpatterns = [
    path('',index,name = "index"),
    path('<int:list_id>/',detail,name='list_detail'),
    path('create/',create,name='list_create'),
    path('<int:list_id>/delete',deleteList,name='list_del'),
    path('<int:list_id>/create',createItem,name='item_create'),
    path('<int:list_id>/<int:item_id>/delete',deleteItem,name='item_del'),
    path('<int:list_id>/<int:item_id>/update',update,name='item_update')
]