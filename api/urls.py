from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('persons', PersonViewSet, basename = 'prsn')
router.register('phone', PhoneViewSet, basename='phne')
router.register('home', HomeViewSet, basename='hme')
router.register('relations', RelationViewSet, basename='relates')

urlpatterns = [
    path('', include(router.urls)),
]