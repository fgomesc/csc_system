from django.urls import path
from apps.estoque.views import EstoqueList, EstoqueDetail

urlpatterns = [
    path('', EstoqueList.as_view(), name='list_estoque'),
    path('detail/<int:pk>/', EstoqueDetail.as_view(), name='estoque_detail'),
]
