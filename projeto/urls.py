from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),

    # Swagger
    path("openapi/", get_schema_view(
        title="PATRI-TECH API",
        description="Documentação da API de inventário de bens",
        version="1.0.0"
    ), name="openapi-schema"),

    path("docs/", TemplateView.as_view(
        template_name="swagger.html"
    ), name="swagger-ui"),
]
