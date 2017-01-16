from Movies_REST Person, Movie, Role
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'screenplay', 'year', 'genre', 'ranking')

