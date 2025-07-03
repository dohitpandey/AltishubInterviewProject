from rest_framework import viewsets

from .apartmentSerializer import ApartmentSerializer
from .models import ApartmentModel


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentSerializer

    def get_queryset(self):

        queryset = ApartmentModel.objects.all()

        # filtering
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__iexact=city)
        min_rent = self.request.query_params.get('min_rent')
        if min_rent:
            queryset = queryset.filter(rent__gte=min_rent)
        max_rent = self.request.query_params.get('max_rent')
        if max_rent:
            queryset = queryset.filter(rent__lte=max_rent)

        # sorting
        allowed_fields = ['apartment_name', 'city', 'rent', 'bedrooms', 'posted_on']
        sort_by = self.request.query_params.get('sort_by', '-posted_on')
        sort_field = sort_by.lstrip('-')
        if sort_field not in allowed_fields:
            sort_by = '-posted_on'
        return queryset.order_by(sort_by, '-posted_on')
