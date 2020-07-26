import random
import string

from django.db import models
from rest_framework.exceptions import ValidationError

from commons.models import SoftDeletionModel
from schools.models import School


# Create your models here.


class Student(SoftDeletionModel):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL, default='FR')
    student_number = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def clean(self):
        import ipdb
        ipdb.set_trace()

        if not self.school:
            raise ValidationError("School is required!")

    def save(self, *args, **kwargs):
        self.student_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        super(Student, self).save(*args, **kwargs)
