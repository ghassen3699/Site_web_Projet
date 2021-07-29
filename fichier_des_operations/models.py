from django.db import models
from operation.models import OperationTerminer



class Fichier_Operation(models.Model) :
    du = models.DateField(verbose_name='Du')
    jusqu_a = models.DateField(verbose_name="Jusqu'a")
    operation = models.ManyToManyField(OperationTerminer , verbose_name="operation")


    def __str__(self) :
        return "Du {} Jusqu'a {}".format(self.du, self.jusqu_a)




