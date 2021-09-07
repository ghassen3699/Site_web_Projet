from django.db import models






class Nationalite (models.Model) :
    nom_nationalite = models.CharField(max_length=50)
    def __str__(self) :
        return self.nom_nationalite





class MigrantIrregulier(models.Model) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    numero_cin = models.CharField(max_length=8,verbose_name="le numero cin",blank=True,unique=True)
    copie_cin = models.ImageField(blank = True)
    numero_passport = models.CharField(max_length=30,blank=True,verbose_name="le numero de passport",unique=True)
    copie_passport = models.ImageField(blank = True,verbose_name="copie passport")


    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme'),
    ) 
    sexe = models.CharField(max_length=30,choices=SEXE) 
    numero_telephone = models.CharField(max_length=8,verbose_name="le numero telephone",blank=True)
    photo_personnel = models.ImageField(blank = True,verbose_name="photo personnel")
    nationalite = models.ForeignKey(Nationalite,on_delete=models.CASCADE)


    capter_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self) :
        return 'Nom: ({}) Prenom: ({}) Cin: ({})'.format(self.nom, self.prenom, self.numero_cin)





