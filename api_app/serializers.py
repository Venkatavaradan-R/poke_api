from rest_framework import serializers
from api_app.models import pokemon,moves

class pokemonSerializer(serializers.ModelSerializer):
    # making is_legendary not required for put method. This can also be done in the model
    is_legendary = serializers.BooleanField(required = False)
    pkmn_name = serializers.CharField(required = False)
    class Meta:
        model = pokemon
        fields = '__all__'


class movesSerializer(serializers.ModelSerializer):
    power = serializers.IntegerField(required = False)
    contact_format = serializers.CharField(required = False)
    move_type = serializers.CharField(required = False)
    move_name = serializers.CharField(required = False)



    class Meta:
        model = moves;
        fields = '__all__'