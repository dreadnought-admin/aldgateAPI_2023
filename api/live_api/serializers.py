from rest_framework import serializers
from .models import Burger, Fish, Chicken, Fries, Snack, Wing, Wrap, Hotdog, Side, Special, TradPack, SpecialPack, Extra

class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = '__all__'

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'

class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = '__all__'

class FriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fries
        fields = '__all__'

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = '__all__'

class WingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wing
        fields = '__all__'

class WrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wrap
        fields = '__all__'

class HotdogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotdog
        fields = '__all__'
        
class SideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Side
        fields = '__all__'

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = '__all__'

class TradPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradPack
        fields = '__all__'

class SpecialPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialPack
        fields = '__all__'

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = '__all__'

