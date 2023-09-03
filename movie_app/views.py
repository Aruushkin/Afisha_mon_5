from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from movie_app.serializers import DirectorSerializers, DirectorDetailSerializers, MovieSerializers, \
    MovieDetailSerializers, ReviewSerializers, ReviewDetailSerializers
from movie_app.models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializers(
        director,
        many=True
    )
    return Response(
        data=serializer.data
    )


@api_view(['GET'])
def director_list_view(request, id):
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


@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializers(movie, many=True)
    return Response(
        data=serializer.data
    )


@api_view(['GET'])
def movie_list_view(request, id):
    try:
        movie_list = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(
            data={'error': 'Movie not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = MovieDetailSerializers(
        movie_list,
        many=False
    )
    return Response(
        data=serializer.data
    )


@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(
        review,
        many=True
    )
    return Response(
        data=serializer.data
    )


@api_view(['GET'])
def review_list_view(request, id):
    try:
        review_list = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={'error': 'Reviews not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = ReviewDetailSerializers(
        review_list,
        many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_views(request):
    movie_list = Movie.objects.all()
    serializer = MovieSerializers(movie_list, many=True).data
    return Response(data=serializer)


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializers(directors, many=True)
    return Response(data=serializer.data)









