from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

SIZE_CHOICES = (
    ('M', 'Medium'),
    ('S', 'Small'),
    ('L', 'Large'),
    ('XL', 'Xtra-large')
)

class Burger(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=True)
    gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Fish(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default=None, null=True)

    def __str__(self):
        return f'{self.name}'

class Chicken(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class Fries(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class Snack(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class Wing(models.Model):
    kilos = models.CharField(max_length=30)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.kilos}'

class Wrap(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class Hotdog(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class Side(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0, null=False)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default=None, null=True)

    def __str__(self):
        return f'{self.name}'

class Special(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250, null=True)
    price = models.FloatField(default=0, null=False)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default=None, null=True)

    def __str__(self):
        return f'{self.name}'

class TradPack(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class SpecialPack(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, null=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

class Extra(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

