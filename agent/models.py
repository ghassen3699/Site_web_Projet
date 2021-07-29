from django.db import models
from grade_de_travail.models import GradeDeTravail
from lieu_de_travail.models import Lieu_De_Travail
from django.contrib.auth import get_user_model



user = get_user_model()

class Agent(models.Model) :


    account_user = models.OneToOneField(user,on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    numero_telephone = models.CharField(max_length=8)
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=5)
    SEXE = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        )
    sexe = models.CharField(max_length=30,choices=SEXE) 
    grade_de_travail_fk = models.OneToOneField(GradeDeTravail,on_delete=models.CASCADE)
    lieu_de_travail_fk = models.OneToOneField(Lieu_De_Travail,on_delete=models.CASCADE)
    numero_cin = models.CharField(max_length=8)
    copie_cin = models.ImageField()
    



    def __str__(self) :
        return '{} {}'.format(self.nom,self.prenom)



