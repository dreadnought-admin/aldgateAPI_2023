from django.contrib import admin
from .models import *

# Register your models here.

class BurgerAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price', 'gluten_free')

    admin.site.register(Burger)

class FishAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price', 'size')

    admin.site.register(Fish)

class ChickenAdmin(admin.ModelAdmin):
    list = ('name', 'price')

    admin.site.register(Chicken)

class FriesAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price')

    admin.site.register(Fries)

class SnackAdmin(admin.ModelAdmin):
    list = ('name','price')

    admin.site.register(Snack)

class WingAdmin(admin.ModelAdmin):
    list = ('kilos', 'price')

    admin.site.register(Wing)

class WrapAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price')

    admin.site.register(Wrap)

class HotdogAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price')

    admin.site.register(Hotdog)

class SideAdmin(admin.ModelAdmin):
    list = ('name', 'price', 'size')

    admin.site.register(Side)

class SpecialAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price', 'size')

    admin.site.register(Special)

class TradPackAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price')

    admin.site.register(TradPack)

class SpecialPackAdmin(admin.ModelAdmin):
    list = ('name', 'description', 'price')

    admin.site.register(SpecialPack)

class ExtraAdmin(admin.ModelAdmin):
    list = ('name','price')

    admin.site.register(Extra)

