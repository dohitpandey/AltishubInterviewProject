from rest_framework import viewsets

from .apartmentSerializer import ApartmentSerializer
from .models import ApartmentModel


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentSerializer
