from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from api.views import CaloriesViewSet, CategoryViewSet, IngredientViewSet, RecipeFilters, RecipeViewSet
from user.views import UserViewSet

router = DefaultRouter()
router.register('recipe', RecipeViewSet)
router.register('category', CategoryViewSet)
router.register('ingredient', IngredientViewSet)
router.register('calories', CaloriesViewSet)
router.register('user', UserViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/recipes-filter/', RecipeFilters.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
