from Movies_REST.models import Person, Movie, Role
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        #fields = ('first_name', 'last_name', 'birth_date', 'birthplace')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'



