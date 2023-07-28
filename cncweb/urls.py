
from django.urls import path
from . import views
from .views import CollectionDetailView  # 'CollectionDetailView' sınıfını import ettik



urlpatterns = [
    path('', views.home, name='home'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('koleksiyonlar/', views.collection_list, name='collection_list'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),

]