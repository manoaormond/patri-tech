from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema

from .models import Bem, Categoria, Status, Unidade, Sala
from .serializers import (
    BemSerializer, CategoriaSerializer, StatusSerializer, 
    UnidadeSerializer, SalaSerializer
)

# --- LOGIN (A peça que estava faltando!) ---
@extend_schema(tags=["Autenticação"])
@api_view(["POST"])
@permission_classes([AllowAny])
def api_login(request):
    """Endpoint para autenticar o usuário no sistema."""
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Login realizado com sucesso"})
    return JsonResponse({"detail": "Credenciais inválidas"}, status=401)

# --- MIXIN DE PERMISSÕES ---
class PatriTechPermissionsMixin:
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

# --- CATEGORIAS ---
@extend_schema(tags=["Categorias"])
class CategoriaListCreateView(PatriTechPermissionsMixin, generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@extend_schema(tags=["Categorias"])
class CategoriaDetailView(PatriTechPermissionsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# --- STATUS ---
@extend_schema(tags=["Status"])
class StatusListCreateView(PatriTechPermissionsMixin, generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

@extend_schema(tags=["Status"])
class StatusDetailView(PatriTechPermissionsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# --- UNIDADES ---
@extend_schema(tags=["Unidades"])
class UnidadeListCreateView(PatriTechPermissionsMixin, generics.ListCreateAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

@extend_schema(tags=["Unidades"])
class UnidadeDetailView(PatriTechPermissionsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

# --- SALAS ---
@extend_schema(tags=["Salas"])
class SalaListCreateView(PatriTechPermissionsMixin, generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

@extend_schema(tags=["Salas"])
class SalaDetailView(PatriTechPermissionsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

# --- BENS ---
@extend_schema(tags=["Bens"])
class BemListCreateView(PatriTechPermissionsMixin, generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

@extend_schema(tags=["Bens"])
class BemDetailView(PatriTechPermissionsMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer