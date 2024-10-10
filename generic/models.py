from django.db import models

# Create your models here.
class GenericModel(models.Model):
    FIRST_TYPE = '1st'
    SECOND_TYPE = '2nd'
    THIRD_TYPE = '3rd'
    
    TYPE_CHOICES = [
        (FIRST_TYPE, 'First Type'),
        (SECOND_TYPE , 'Second Type'),
        (THIRD_TYPE , 'Third Type'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    exceptional = models.BooleanField()