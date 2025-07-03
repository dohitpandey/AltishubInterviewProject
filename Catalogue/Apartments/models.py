from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ApartmentModel(models.Model):
    apartment_name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
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
    posted_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.city:
            self.city = self.city.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.apartment_name
