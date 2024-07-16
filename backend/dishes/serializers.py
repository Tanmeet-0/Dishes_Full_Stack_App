from rest_framework import serializers
from .models import Dish

class DishSerializer(serializers.Serializer):
    dishId = serializers.IntegerField()
    dishName = serializers.CharField()
    imageUrl = serializers.CharField()
    isPublished = serializers.BooleanField()

    def create(self,validated_data):
        return Dish.objects.create(**validated_data)