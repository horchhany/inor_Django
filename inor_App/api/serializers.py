from rest_framework import serializers
from inor_App.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=2000)
    avtive = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)