from rest_framework import serializers
from .models import Type, Todo


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'status')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'type', 'title', 'description', 'completed', 'created_date')