from django.urls import path
from . import views


urlpatterns = [
    path("billets/", views.BilletView.as_view()),
    path("users/<uuid:pk>/billets/", views.BilletIdView.as_view())
]
