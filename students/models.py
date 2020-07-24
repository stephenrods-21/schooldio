import random
import string

from django.db import models
from commons.models import SoftDeletionModel
from schools.models import School


# Create your models here.


class Student(SoftDeletionModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.student_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
        super(Student, self).save(*args, **kwargs)
