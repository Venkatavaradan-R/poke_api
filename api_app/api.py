from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_app.serializers import *

class pokemonList(APIView):
    def get(self, request):
        model = pokemon.objects.all()
        serializer = pokemonSerializer(model ,many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = pokemonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class pokemonDetails(APIView):
    def get(self, request, pk):
        model = pokemon.objects.get(pokedex_id = pk)
        serializer = pokemonSerializer(model )
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = pokemonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class movesList(APIView):
    def get(self,request):
        model = moves.objects.all()
        serializer = movesSerializer(model, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = movesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)