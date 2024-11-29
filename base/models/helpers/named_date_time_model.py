from django.db import models
from .date_time_model import DateTimeModel

class NamedDateTimeModel(DateTimeModel):

    name = models.CharField(max_length=180)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name