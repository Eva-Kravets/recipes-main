from rest_framework.serializers import ModelSerializer
from .models import Recipe, Category, Ingredient, Calories


class CaloriesSerializer(ModelSerializer):
    class Meta:
        model = Calories
        fields = '__all__'


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    categories = CategorySerializer(source='category', many=True)
    ingredients_data = IngredientSerializer(source='ingredients', many=True)
    class Meta:
        model = Recipe
        # fields = '__all__'
        exclude = ['category', 'ingredients']
