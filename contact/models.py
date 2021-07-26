from django.db import models




class Contact(models.Model) :
    nom = models.CharField(max_length=50)
    adresse_mail = models.EmailField()
    sujet  = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.nom