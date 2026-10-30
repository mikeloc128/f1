from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Phone(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE, related_name='phones')
    number = PhoneNumberField(region="UZ")
    label = models.CharField(max_length=20, default="Mobile")

    def __str__(self):
        return f"{self.label}: {self.number}"
