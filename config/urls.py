"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("retailapp/", include("retailapp.urls")),
]

from django.http import HttpResponse
import requests

def proxy_superset(request, path):
    superset_url = f"http://localhost:8088/{path}"
    headers = {
        key: value for key, value in request.headers.items() if key.lower() != "host"
    }
    response = requests.get(superset_url, headers=headers)
    django_response = HttpResponse(
        response.content, status=response.status_code, content_type=response.headers.get("Content-Type")
    )
    for key, value in response.headers.items():
        if key.lower() not in ["content-encoding", "transfer-encoding", "content-length"]:
            django_response[key] = value
    return django_response
