from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics
from django.db.models import Q
import django_filters.rest_framework
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer, CaloriesSerializer
from .models import Recipe, Category, Ingredient, Calories


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CaloriesViewSet(ReadOnlyModelViewSet):
    queryset = Calories.objects.all()
    serializer_class = CaloriesSerializer

class RecipeViewSet(ReadOnlyModelViewSet):
    queryset = Recipe.objects.filter(visible=True)
    serializer_class = RecipeSerializer


class RecipeFilters(generics.ListAPIView):
    queryset = Recipe.objects.filter(Q(visible=True), Q(ingredients__name='Огурец'))
    serializer_class = RecipeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'category']