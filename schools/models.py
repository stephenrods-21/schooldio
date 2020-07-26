from django.db import models

# Create your models here.
from commons.models import SoftDeletionModel


def upload_path(instance, filename):
    return '/'.join(['school-pic', str(instance.name), filename])


class School(SoftDeletionModel):
    name = models.CharField(max_length=20)
    max_students = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return f'{self.name}'
