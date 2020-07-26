from django.db.models import Q
from rest_framework import serializers


def build_nested_query(kwargs):
    query = Q()
    try:
        if 'pk' in kwargs:
            query = Q(pk=int(kwargs.get('pk')))
        if 'school_pk' in kwargs:
            query = query & Q(school_id=int(kwargs.get('school_pk')))
    except KeyError as ex:
        raise serializers.ValidationError({"detail": "key not found"})

    return query


def get_school_id_param(request, kwargs):
    if 'school_pk' in kwargs:
        school_id = int(kwargs['school_pk'])
    else:
        school_id = int(request.data['school'])
    return school_id
