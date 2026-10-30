from rest_framework import serializers
from django.utils import timezone
from persons.models import Person
from locations.models import Home
from phones.models import Phone
from relations.models import Relation

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id','person', 'number', 'label']
        
        def validate_birth_date(self, value):
            current_year = timezone.now().year

            if value.year < 1800:
                raise serializers.ValidationError(
                    "Birth year cannot be earlier than 1800."
                )

            if value.year > current_year:
                raise serializers.ValidationError(
                    "Birth date cannot be in the future."
                )

            return value


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ['id', 'person', 'related_person', 'relation_type']


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'person', 'address_line']


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)
    addresses = HomeSerializer(many=True, read_only=True)
    outbound_relations = RelationSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = [
            'id', 'surname', 'name', 'patronymic', 
            'birth_date', 'phones', 'addresses', 
            'outbound_relations'
            ]



