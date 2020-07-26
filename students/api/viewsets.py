from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django_filters.rest_framework import filters, DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from schools.models import School
from students.api.serializers import StudentSerializer
from students.filter import StudentSearchFilter
from students.models import Student
from students.utils import build_nested_query


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentSearchFilter  # here
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['first_name', 'last_name', ]

    def get_queryset(self):
        query = build_nested_query(self.kwargs)
        return Student.objects.filter(query)

    def create(self, request, *args, **kwargs):
        student_data = request.data

        if 'school_pk' in kwargs:
            school_id = int(kwargs['school_pk'])
        else:
            school_id = int(student_data['school'])

        student_serializer = StudentSerializer(data=request.data)

        if not student_serializer.is_valid():
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            school = School.objects.get(id=school_id)
        except ObjectDoesNotExist:
            return Response({'error_msg': 'school not found'}, status=status.HTTP_404_NOT_FOUND)

        student_count = Student.objects.filter(school_id=school_id).count()

        if student_count >= school.max_students:
            return Response({'error_msg': 'Max capacity reached'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        new_student = Student.objects.create(first_name=student_data['first_name'], last_name=student_data['last_name'],
                                             school_id=school_id)
        new_student.clean()
        new_student.save()

        serializer = StudentSerializer(new_student)
        return Response(serializer.data)
