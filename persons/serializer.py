from rest_framework import serializers 
from .model import Person

class PersonSerializer(serializers.ModelSerializer):
    model = Person
    fields = ['surname', 'name', 'patronymic']