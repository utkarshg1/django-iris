from django.db import models
from django.core.validators import MinValueValidator


class IrisData(models.Model):
    sepal_length = models.FloatField(MinValueValidator(0))
    sepal_width = models.FloatField(MinValueValidator(0))
    petal_length = models.FloatField(MinValueValidator(0))
    petal_width = models.FloatField(MinValueValidator(0))
    species = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.species
