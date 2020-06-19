from rest_framework import serializers
from api_app.models import pokemon

class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemon
        fields = '__all__'