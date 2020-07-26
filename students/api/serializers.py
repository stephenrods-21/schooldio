from rest_framework import serializers

from schools.api.serializers import SchoolSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'student_number', 'year_in_school', 'school')
        read_only_fields = ['student_number',]

