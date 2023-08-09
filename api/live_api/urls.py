from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from live_api import views
from v1_api.views import MenuItemViewSet, PackViewSet, ExtraViewSet

# router = DefaultRouter()
# router.register(r'menu', MenuItemViewSet, basename='menu')
# router.register(r'extras', ExtraViewSet, basename='extra')
# router.register(r'packs', PackViewSet, basename='pack')
# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views, name="home"),
    path('menu/', MenuItemViewSet.as_view({'get': 'list'})),
    path('extras/', ExtraViewSet.as_view({'get': 'list'})),
    path('packs/', PackViewSet.as_view({'get': 'list'}))
]