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

# --- LOGIN ---
@extend_schema(tags=["Autenticação"])
@api_view(["POST"])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Login realizado com sucesso"})
    return JsonResponse({"detail": "Credenciais inválidas"}, status=401)

# --- BENS ---
@extend_schema(tags=["Bens"])
class BemListCreateView(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
    def get_permissions(self):
        if self.request.method == "GET": return [AllowAny()]
        return [IsAuthenticated()]

@extend_schema(tags=["Bens"])
class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
    permission_classes = [IsAuthenticated]

# --- CATEGORIAS ---
@extend_schema(tags=["Categorias"])
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    def get_permissions(self):
        if self.request.method == "GET": return [AllowAny()]
        return [IsAuthenticated()]

# --- STATUS ---
@extend_schema(tags=["Status"])
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    def get_permissions(self):
        if self.request.method == "GET": return [AllowAny()]
        return [IsAuthenticated()]

# --- UNIDADES ---
@extend_schema(tags=["Unidades"])
class UnidadeListCreateView(generics.ListCreateAPIView):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    def get_permissions(self):
        if self.request.method == "GET": return [AllowAny()]
        return [IsAuthenticated()]

# --- SALAS ---
@extend_schema(tags=["Salas"])
class SalaListCreateView(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    def get_permissions(self):
        if self.request.method == "GET": return [AllowAny()]
        return [IsAuthenticated()]