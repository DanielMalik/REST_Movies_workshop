from django.shortcuts import render
from Movies_REST.serializers import MovieSerializer, PersonSerializer
from Movies_REST.models import Movie, Person
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404

# Create your views here.

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


#
#
# class PersonList(APIView):
#
#     def get(self, request, format=None):
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True, context={'request': request})
#         return Response(serializer.data)
#
#
# class MoviesList(APIView):
#
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = MovieSerialiezer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, ststus=HTTP_400_BAD_REQUEST)
#
# class PersonDetail(APIView):
#     def get_object(self, pk):
#
#         try:
#             return Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         person = self.get_object(pk)
#         serializer = PersonSerializer(person, context={"request": request})
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#
#         person = self.get_object(pk)
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk, format=None):
#         person = self.get_object(pk)
#         serializer = PersonSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class MovieDetail(APIView):
#
#     def get_object(self, pk):
#
#         try:
#             return Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, context={"request": request})
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

