from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ApartmentModel(models.Model):
    apartment_name = models.CharField(max_length=50)
    rent = models.DecimalField(
        max_digits=5,
        decimal_places=0,
        validators=[
            MinValueValidator(15000),
            MaxValueValidator(25000)]
    )
    bedrooms = models.DecimalField(
        max_digits=1,
        decimal_places=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3)]
    )

    def __str__(self):
        return self.apartment_name
