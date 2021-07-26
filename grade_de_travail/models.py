from django.db import models



class GradeDeTravail(models.Model) :
    nom_grade = models.CharField(max_length=50)


    def __str__(self) :
        return self.nom_grade




