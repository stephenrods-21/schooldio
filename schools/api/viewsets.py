from rest_framework import viewsets
from schools.api.serializers import SchoolSerializer
from schools.models import School


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return School.objects.filter(student=self.kwargs['student_pk'])
