"""
    consequence URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

from consequence.router_urls import router_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_urlpatterns)),
    path('api/accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema', get_schema_view(
        title="True Layer Auth",
        version="1.0.0",
        permission_classes=(permissions.AllowAny,)
    ), name='openapi-schema'),
    path('api/swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]