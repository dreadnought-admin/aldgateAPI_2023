from rest_framework import viewsets
from .serializers import BurgerSerializer, FishSerializer, ChickenSerializer, FriesSerializer, SnackSerializer, WingSerializer, WrapSerializer, HotdogSerializer, SideSerializer, SpecialSerializer, TradPackSerializer, SpecialPackSerializer, ExtraSerializer
from .models import Burger, Fish, Chicken, Fries, Snack, Wing, Wrap, Hotdog, Side, Special, TradPack, SpecialPack, Extra 

class BurgerViewSet(viewsets.ModelViewSet):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer

class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class ChickenViewSet(viewsets.ModelViewSet):
    queryset = Chicken.objects.all()
    serializer_class = ChickenSerializer

class SnackViewSet(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class WingViewSet(viewsets.ModelViewSet):
    queryset = Wing.objects.all()
    serializer_class = WingSerializer

class FriesViewSet(viewsets.ModelViewSet):
    queryset = Fries.objects.all()
    serializer_class = FriesSerializer

class WrapViewSet(viewsets.ModelViewSet):
    queryset = Wrap.objects.all()
    serializer_class = WrapSerializer

class HotdogViewSet(viewsets.ModelViewSet):
    queryset = Hotdog.objects.all()
    serializer_class = HotdogSerializer

class SideViewSet(viewsets.ModelViewSet):
    queryset = Side.objects.all()
    serializer_class = SideSerializer

class SpecialViewSet(viewsets.ModelViewSet):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

class TradPackViewSet(viewsets.ModelViewSet):
    queryset = TradPack.objects.all()
    serializer_class = TradPackSerializer

class SpecialPackViewSet(viewsets.ModelViewSet):
    queryset = SpecialPack.objects.all()
    serializer_class = SpecialPackSerializer

class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


