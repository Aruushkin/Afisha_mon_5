from movie_app.models import Director, Movie, Review
from rest_framework import serializers


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class DirectorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    Director = DirectorSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'director name'.split()


class MovieDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'