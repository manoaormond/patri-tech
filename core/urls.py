from django.urls import path
from .views import (
    api_login,
    CategoriaListCreateView, CategoriaDetailView,
    StatusListCreateView, StatusDetailView,
    UnidadeListCreateView, UnidadeDetailView,
    SalaListCreateView, SalaDetailView,
    BemListCreateView, BemDetailView
)

urlpatterns = [
    path("login/", api_login, name="api-login"),
    
    # Categorias
    path("categorias/", CategoriaListCreateView.as_view(), name="categoria-list"),
    path("categorias/<int:pk>/", CategoriaDetailView.as_view(), name="categoria-detail"),
    
    # Status
    path("status/", StatusListCreateView.as_view(), name="status-list"),
    path("status/<int:pk>/", StatusDetailView.as_view(), name="status-detail"),
    
    # Unidades
    path("unidades/", UnidadeListCreateView.as_view(), name="unidade-list"),
    path("unidades/<int:pk>/", UnidadeDetailView.as_view(), name="unidade-detail"),
    
    # Salas
    path("salas/", SalaListCreateView.as_view(), name="sala-list"),
    path("salas/<int:pk>/", SalaDetailView.as_view(), name="sala-detail"),
    
    # Bens
    path("bens/", BemListCreateView.as_view(), name="bem-list"),
    path("bens/<int:pk>/", BemDetailView.as_view(), name="bem-detail"),
]