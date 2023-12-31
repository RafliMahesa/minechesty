from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tambah/<int:id>/', tambah_amount, name='tambah_amount'),
    path('kurang/<int:id>/', kurang_amount, name='kurang_amount'),
    path('hapus/<int:id>/', hapus_item, name='hapus_item'),
    path('edit-product/<int:id>', edit_item, name='edit_product'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete-ajax/<int:id>/',delete_item_ajax,name='delete_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]