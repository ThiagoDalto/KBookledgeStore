from django.urls import path
from . import views

urlpatterns = [
    path("books/<uuid:pk>/orders/", views.OrderView.as_view()),
    path("orders/<uuid:pk>/", views.OrderIdView.as_view()),
    path("orders/", views.OrderView.as_view()),
]
