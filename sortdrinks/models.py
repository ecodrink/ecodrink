from django.db import models
from django.utils import timezone


class Drink(models.Model):

    item_id = models.IntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)

    name = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    style = models.ForeignKey('Style', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    organic = models.BooleanField()

    price = models.FloatField()
    volume = models.FloatField()
    alcohol_percent = models.FloatField()

    score = models.FloatField()

    @property
    def is_new(self):
        if self.date_added > timezone.localdate() - timezone.timedelta(weeks=2):
            return True
        return False

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['score']


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Style(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
