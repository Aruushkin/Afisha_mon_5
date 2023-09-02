from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.db.models import Count

# from rest_framework import r
from rest_framework import status
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_list_api_view(request):
    director = Director.objects.all()
    data = DirectorSerializer(instance=director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_api_view(request, director_id):
    director = Director.objects.get(id=director_id)
    data = DirectorSerializer(instance=director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()
    data = MovieSerializer(instance=movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = MovieSerializer(instance=movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(instance=review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    review = Review.objects.get(id=review_id)
    data = ReviewSerializer(instance=review, many=False).data
    return Response(data=data)










