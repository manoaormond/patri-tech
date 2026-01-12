from django.urls import path
from .views import (
    api_login,
    BemListCreateView, 
    BemDetail, 
    CategoriaListCreateView, 
    StatusListCreateView,
    UnidadeListCreateView, 
    SalaListCreateView
)

urlpatterns = [
    path("login/", api_login, name="api-login"),
    path("bens/", BemListCreateView.as_view(), name="bens-list"),
    path("bens/<int:pk>/", BemDetail.as_view(), name="bens-detail"),
    path("categorias/", CategoriaListCreateView.as_view(), name="categorias-list"),
    path("status/", StatusListCreateView.as_view(), name="status-list"),
    path("unidades/", UnidadeListCreateView.as_view(), name="unidades-list"),
    path("salas/", SalaListCreateView.as_view(), name="salas-list"),
]