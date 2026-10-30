from django.db import models

# Create your models here.
class Home(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE, related_name="address")
    address_line = models.CharField(max_length = 255)

    def __str__(self):
        return f"self.person"
