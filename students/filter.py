from django_filters import rest_framework as filters
from django.db.models import Q

from students.models import Student


class StudentSearchFilter(filters.FilterSet):
    name = filters.CharFilter(method='name_filter')

    class Meta:
        model = Student
        fields = ('first_name', 'last_name',)

    @staticmethod
    def name_filter(queryset, name, value):
        name_list = [v.strip() for v in value.split()]
        query_params = Q()
        for v in name_list:
            query_params.add(Q(first_name__icontains=v), Q.OR)
            query_params.add(Q(last_name__icontains=v), Q.OR)
        return queryset.filter(query_params)
