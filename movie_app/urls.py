from django.urls import path
from .views import DirectorListView, DirectorDetailView, MovieListView, MovieDetailView, \
    ReviewListView, ReviewDetailView, MoviesView, DirectorsView

urlpatterns = [
    path('directors/', DirectorListView.as_view()),
    path('directors/<int:id>/', DirectorDetailView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:id>/', MovieDetailView.as_view()),
    path('reviews/', ReviewListView.as_view()),
    path('reviews/<int:id>/', ReviewDetailView.as_view()),
    path('movies_views/', MoviesView.as_view()),
    path('directors_views/', DirectorsView.as_view()),
]
