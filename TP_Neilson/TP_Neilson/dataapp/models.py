from django.db import models

class Employee(models.Model):
    departement_choices = [
        ('Marketing', 'Marketing'),
        ('RH', 'RH'),
        ('Ventes', 'Ventes'),
        ('IT', 'IT'),
        ('R&D', 'R&D'),
    ]
    
    evaluation_choices = [
        ('Faible', 'Faible'),
        ('Moyenne', 'Moyenne'),
        ('Elevée', 'Elevée'),
    ]

    ID = models.PositiveIntegerField(primary_key=True)
    anciennete = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    paiement = models.DecimalField(max_digits=10, decimal_places=2)
    departement = models.CharField(max_length=50, choices=departement_choices)
    evaluation = models.CharField(max_length=10, choices=evaluation_choices)

    def __str__(self):
        return f"Employee {self.ID}"
