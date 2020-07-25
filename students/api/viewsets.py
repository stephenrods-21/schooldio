from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response

from schools.models import School
from students.api.serializers import StudentSerializer
from students.filter import StudentSearchFilter
from students.models import Student


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    filterset_class = StudentSearchFilter  # here
    queryset = Student.objects.all()

    def get_queryset(self):
        query = Q()
        if 'pk' in self.kwargs:
            query = Q(pk=self.kwargs['pk'])
        if 'school_pk' in self.kwargs:
            query = query & Q(school_id=self.kwargs['school_pk'])
        return Student.objects.filter(query)

    def create(self, request, *args, **kwargs):
        student_data = request.data

        try:
            school_id = int(student_data['school'])
            school = School.objects.get(id=school_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student_count = Student.objects.filter(school_id=school_id).count()

        if student_count == school.max_students:
            return Response({'error': 'Max capacity reached!'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        new_student = Student.objects.create(first_name=student_data['first_name'], last_name=student_data['last_name'],
                                             school_id=student_data['school'])
        new_student.save()

        serializer = StudentSerializer(new_student)
        return Response(serializer.data)
