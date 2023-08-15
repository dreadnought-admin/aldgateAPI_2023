"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import routers

# router = routers.DefaultRouter()
# # from live_api import urls as api_urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.site.urls),
#     path('api-auth', include('rest_framework.urls')),
#     # path('api/', include(api_urls))
# ]

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from live_api.views import *

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
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls)
]