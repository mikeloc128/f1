from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from persons.models import Person
from locations.models import Home
from phones.models import Phone
from relations.models import Relation
from .serializers import *

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.prefetch_related('phones', 'address', 'outbound_relations', 'inbound_relations').all()
    serializer_class = PersonSerializer


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class RelationViewSet(viewsets.ModelViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer




