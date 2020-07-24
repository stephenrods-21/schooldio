from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'student_number', 'school')
        read_only_fields = ['student_number']

        def create(self, validated_data):
            import ipdb
            ipdb.set_trace()
