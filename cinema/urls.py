from django.urls import path
from . import views

urlpatterns = [
    path("api/movies/", views.movie_list, name="movie-list-api"),
    path("api/movies/<int:pk>/", views.movie_detail, name="movie-detail-api"),
    path("api/movies/create/", views.movie_create, name="movie-create-api"),
    path("api/movies/<int:pk>/update/", views.movie_update, name="movie-update-api"),
    path("api/movies/<int:pk>/delete/", views.movie_delete, name="movie-delete-api"),
]

app_name = "cinema"
