from rest_framework import serializers
from .models import ApartmentModel


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentModel
        fields = '__all__'
