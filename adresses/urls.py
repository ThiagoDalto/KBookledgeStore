from django.urls import path
from . import views


urlpatterns = [
    path("users/address/", views.AddressView.as_view()),
    path("users/address/<uuid:pk>/", views.AddressDetailView.as_view()),
]
