from django.db import models

# Create your models here.
from commons.models import SoftDeletionModel


class School(SoftDeletionModel):
    name = models.CharField(max_length=20)
    max_students = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

