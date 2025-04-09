from rest_framework import serializers
from .models import Type, Todo

class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('status',)

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'created_date')
