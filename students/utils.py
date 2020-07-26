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
