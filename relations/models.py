from django.db import models

# Create your models here.
class Relation(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE, related_name = 'outbound_relations')
    related_person = models.ForeignKey('persons.Person', on_delete=models.CASCADE, related_name = "inbound_relations")
    relation_type = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.person} > {self.relation_type} > {self.related_person}"