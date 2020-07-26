from django.core.exceptions import ObjectDoesNotExist
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from schools.api.serializers import SchoolSerializer
from schools.filter import SchoolSearchFilter
from schools.models import School


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = SchoolSerializer
    filterset_class = SchoolSearchFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['name', 'max_students']

    def create(self, request, *args, **kwargs):
        school_data = request.data

        school_serializer = SchoolSerializer(data=school_data)
        if not school_serializer.is_valid():
            return Response(school_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_school = School.objects.create(name=school_data['name'], max_students=school_data['max_students'],
                                           image=school_data['image'])
        new_school.save()

        serializer = SchoolSerializer(new_school)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        school_data = request.data

        school_serializer = SchoolSerializer(data=school_data)
        if not school_serializer.is_valid():
            return Response(school_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            school = School.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error_msg': 'school not found'}, status=status.HTTP_404_NOT_FOUND)

        school.name = school_serializer.data.get('name')
        school.max_students = school_serializer.data.get('max_students')
        if school_data['image']:
            school.image = school_data['image']
        school.save()

        serializer = SchoolSerializer(school)
        return Response(serializer.data)
