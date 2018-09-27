from django.db import models


class Drink(models.Model):

    item_id = models.IntegerField(unique=True)

    name = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    style = models.ForeignKey('Style', on_delete=models.CASCADE, null=True)
    organic = models.BooleanField()

    price = models.FloatField()
    volume = models.FloatField()
    alcohol_percent = models.FloatField()

    score = models.FloatField()

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
