import django_filters

from .models import Service


class ServiseFilter(django_filters.FilterSet):

    category__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['category__name']