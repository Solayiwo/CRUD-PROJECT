from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    if not re.match(r'^\+\d{1,15}$', value):
        raise ValidationError('Phone number must start with "+" and followed by the country code and digits.')

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=16, validators=[validate_phone_number])
    Location = models.CharField(max_length=255)
    Hobby = models.CharField(max_length=255)


    def __str__(self) -> str:
        return "{} {}".format(self.First_name, self.Last_name)
