from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<slug:category_slug>/', views.item_list, name='item_list_by_category'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('report/', views.report_item, name='report_item'),
    path('claim/<int:item_id>/', views.claim_item, name='claim_item'),
]