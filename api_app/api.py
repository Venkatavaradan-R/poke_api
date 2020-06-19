from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_app.serializers import *

class pokemonList(APIView):
    def get(self, request):
        model = pokemon.objects.all()
        serializer = pokemonSerializer(model ,many = True)
        return Response(serializer.data)