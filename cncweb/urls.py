
from django.urls import path
from . import views
from .views import CollectionDetailView  # 'CollectionDetailView' sınıfını import ettik



# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.hakkimizda, name='about'),  # 'about' is English for 'hakkimizda'
#     path('contact/', views.iletisim, name='contact'),  # 'contact' is English for 'iletisim'
#     path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
#     path('products/<int:product_id>/', views.product_detail, name='product_detail'),
#     path('collections/', views.collection_list, name='collection_list'),  # 'collections' is already in English
#     path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),
#     path('products/', views.product_list, name='product_list'),
# ]
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.hakkimizda, name='about'),
    path('contact/', views.iletisim, name='contact'),
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail_view'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
]
