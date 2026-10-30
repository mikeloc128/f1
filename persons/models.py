from django.db import models

# Create your models here.
class Person(models.Model):
    surname = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    patronymic = models.CharField(max_length = 25, blank=True, null=True)

    birth_date = models.DateField(verbose_name = 'Date of Birth')

    def __str__(self):
        return f"{self.name} {self.surname}"

