from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializers, DirectorDetailSerializers, MovieSerializers, \
    MovieDetailSerializers, ReviewSerializers, ReviewDetailSerializers
from .models import Director, Movie, Review

class DirectorListView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializers(
            directors,
            many=True
        )
        return Response(
            data=serializer.data
        )

class DirectorDetailView(APIView):
    def get(self, request, id):
        try:
            director = Director.objects.get(id=id)
        except Director.DoesNotExist:
            return Response(
                data={'error': 'Director not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DirectorDetailSerializers(
            director,
            many=False
        )
        return Response(
            data=serializer.data
        )

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(
            data=serializer.data
        )

class MovieDetailView(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response(
                data={'error': 'Movie not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieDetailSerializers(
            movie,
            many=False
        )
        return Response(
            data=serializer.data
        )

class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializers(
            reviews,
            many=True
        )
        return Response(
            data=serializer.data
        )

class ReviewDetailView(APIView):
    def get(self, request, id):
        try:
            review = Review.objects.get(id=id)
        except Review.DoesNotExist:
            return Response(
                data={'error': 'Review not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ReviewDetailSerializers(
            review,
            many=False
        )
        return Response(data=serializer.data)

class MoviesView(APIView):
    def get(self, request):
        movie_list = Movie.objects.all()
        serializer = MovieSerializers(movie_list, many=True).data
        return Response(data=serializer)

class DirectorsView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializers(directors, many=True)
        return Response(data=serializer.data)
