from lieu_de_travail.models import Commissariat_De_Police, Province, Region
from django.db import models
from migrant_irregulier.models import MigrantIrregulier


class OperationTerminer(models.Model) :

    nom_operation = models.CharField(max_length=200,verbose_name="le nom de l'operation",blank=True,unique=True)
    date_operation = models.DateField(verbose_name="la date de l'operation")
    nombre_des_migrants = models.IntegerField(verbose_name="le nombres des migrants")
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commissariat = models.ForeignKey(Commissariat_De_Police,on_delete=models.CASCADE)
    NATURE_OPERATION = (
        ('Terre', 'Terre'),
        ('Mer', 'Mer'),
        )
    nature_operation = models.CharField(max_length=30,choices=NATURE_OPERATION,default=None) 
    les_migrants = models.ManyToManyField(MigrantIrregulier)
    
    def __str__(self) :
        return 'Le {} à {}'.format(self.date_operation,self.region)




