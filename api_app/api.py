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
    def get_pokemon(self, pk):
        try:
            model = pokemon.objects.get(pokedex_id = pk)
            return model
        except:
            return

    def get(self, request, pk):
        
        if not self.get_pokemon(pk):
            return Response(f"PK = {pk} not valid", status = status.HTTP_404_NOT_FOUND)

        model = self.get_pokemon(pk)
        serializer = pokemonSerializer(model)
        return Response(serializer.data)


    def put(self, request, pk):

        model = self.get_pokemon(pk)
        serializer = pokemonSerializer(model, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model = self.get_pokemon(pk)
        model.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




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

class movesDetails(APIView):
    def get_move(self, pk):
        try:
            model = moves.objects.get(move_id = pk)
            return model
        except:
            return

    def get(self,request,pk):
        if not self.get_move(pk):
            return Response(f"PK = {pk} not valid", status = status.HTTP_404_NOT_FOUND)
        model = self.get_move(pk)
        serializer = movesSerializer(model)
        return Response(serializer.data)
    
    def put(self,request,pk):

        model = self.get_move(pk)    
        serializer = movesSerializer(model, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        model = self.get_move(pk)
        model.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
