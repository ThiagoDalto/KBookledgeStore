from django.urls import path
from . import views

urlpatterns = [
    path("users/authors/", views.AuthorsView.as_view()),
    path("users/authors/<str:pk>/", views.AuthorsDetailView.as_view())
]
