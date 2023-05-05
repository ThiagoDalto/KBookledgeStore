from django.urls import path
from . import views

urlpatterns = [
    path("paymounts/", views.PaymountsView.as_view()),
    path("paymounts/<uuid:pk>", views.PaymountsIdView.as_view()),
]
