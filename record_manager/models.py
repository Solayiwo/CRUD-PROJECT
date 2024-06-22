from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+666666666'. up to 15 digits allowed."
)


class Student(models.Model):
    id = models.CharField(max_length=20)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    Location = models.CharField(max_length=255)
    Hobby = models.CharField(max_length=255)


    def __str__(self) -> str:
        return "{} {}".format(self.First_name, self.Last_name)
