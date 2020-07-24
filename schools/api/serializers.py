from rest_framework import serializers

from schools.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'max_students')
