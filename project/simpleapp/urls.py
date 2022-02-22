from django.urls import path
from .views import ProductList, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductList.as_view()),
    # Ссылка на детали товара
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # Ссылка на создание товара
    path('create/', ProductCreateView.as_view(), name='product_create'),
    # Ссылка на изменение товара
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    # Ссылка на удаление товара
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
