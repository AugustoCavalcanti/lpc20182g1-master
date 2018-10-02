from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos_estatisticas'),
    path('cliente/<int:cliente_id>/', cliente, name='cliente'),
    path('cliente/estatistica/', cliente_estatisticas, name='cliente_estatisticas'),
]
