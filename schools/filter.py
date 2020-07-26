from django_filters import rest_framework as filters
from django.db.models import Q

from schools.models import School


class SchoolSearchFilter(filters.FilterSet):
    name = filters.CharFilter(method='name_filter', label='School Name')

    class Meta:
        model = School
        fields = ('name',)

    @staticmethod
    def name_filter(queryset, name, value):
        name_list = [v.strip() for v in value.split()]
        query_params = Q()
        for v in name_list:
            query_params.add(Q(name__icontains=v), Q.OR)
        return queryset.filter(query_params)
