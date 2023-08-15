from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import routers
from live_api import views
from .views import *

router = routers.DefaultRouter()

router.register(r'burgers', BurgerViewSet)
router.register(r'chicken', ChickenViewSet)
router.register(r'fish', FishViewSet)
router.register(r'fries', FriesViewSet)
router.register(r'snack', SnackViewSet)
router.register(r'wings', WingViewSet)
router.register(r'wraps', WrapViewSet)
router.register(r'hotdogs', HotdogViewSet)
router.register(r'sides', SideViewSet)
router.register(r'specials', SpecialViewSet)
router.register(r'tradpacks', TradPackViewSet)
router.register(r'specialpacks', SpecialPackViewSet)
router.register(r'extras', ExtraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]


