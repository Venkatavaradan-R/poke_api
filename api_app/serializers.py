from rest_framework import serializers
from api_app.models import pokemon,moves

class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemon
        fields = '__all__'


class movesSerializer(serializers.ModelSerializer):
    class Meta:
        model = moves;
        fields = '__all__'