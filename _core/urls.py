"""_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerSplitView

urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/', include("users.urls")),
    path('api/', include("authors.urls")),
    path('api/', include("adresses.urls")),
    path("api/", include("books.urls")),
    path("api/", include("orders.urls")),
    path("api/", include("paymounts.urls")),
    path("api/", include("billets.urls")),
    path("api/", include("promotions.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerSplitView.as_view(url_name="schema"),
        name="docs-ui",
    ),
]
