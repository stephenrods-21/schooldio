from django_filters import rest_framework as filters
from django.db.models import Q

from students.models import Student


class StudentSearchFilter(filters.FilterSet):
    first_name = filters.CharFilter(method='first_name_filter', label='First Name')
    last_name = filters.CharFilter(method='last_name_filter', label='Last Name')
    full_name = filters.CharFilter(method='full_name_filter', label='Full Name')

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'full_name', 'year_in_school')

    @staticmethod
    def first_name_filter(queryset, name, value):
        name_list = [v.strip() for v in value.split()]
        query_params = Q()
        for v in name_list:
            query_params.add(Q(first_name__icontains=v), Q.OR)
        return queryset.filter(query_params)

    @staticmethod
    def last_name_filter(queryset, name, value):
        name_list = [v.strip() for v in value.split()]
        query_params = Q()
        for v in name_list:
            query_params.add(Q(last_name__icontains=v), Q.OR)
        return queryset.filter(query_params)

    @staticmethod
    def full_name_filter(queryset, name, value):
        name_list = [v.strip() for v in value.split()]
        query_params = Q()
        for v in name_list:
            query_params.add(Q(first_name__icontains=v), Q.OR)
            query_params.add(Q(last_name__icontains=v), Q.OR)
        return queryset.filter(query_params)
