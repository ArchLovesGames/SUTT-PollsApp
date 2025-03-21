from django.urls import path
from . import views  # Ensure you're correctly importing views

urlpatterns = [
    path("", views.index, name="index"),  # Ensure `views.index` exists in views.py
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


