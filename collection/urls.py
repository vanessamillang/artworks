from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artwork/<int:artwork_id>", views.artwork, name="artwork"),
    path('artwork/artist/<int:artist_id>', views.artist_detail, name='artist_detail'),
    path("artworks/search", views.search_artworks, name="search_artworks"),
    path("artworks/random", views.random_artworks, name="random_artworks"),
    path("collections/", views.collections, name="collections"),
    path("collection_list/", views.collection_list, name="collection_list"),
    path("collection/add", views.collection_add, name="collection_add"),
    path("accounts/profile/", views.index, name="index"),
    path("accounts/register/", views.register, name="register")
]