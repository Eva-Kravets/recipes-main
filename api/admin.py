from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Recipe, RecipeImage, Category, Ingredient, Calories


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 2


class RecipeAdmin(admin.ModelAdmin):
    inlines = [ RecipeImageInline, ]

@admin.register(Recipe)
class RecipeAdmin(SimpleHistoryAdmin, ImportExportModelAdmin, RecipeAdmin):
    class Meta:
        proxy = True

@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Ingredient)
class IngredientAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Calories)
class CaloriesAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True
