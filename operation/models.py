from lieu_de_travail.models import Commissariat_De_Police, Province, Region
from agent.models import Agent
from django.db import models








class OperationTerminer(models.Model) :

    nom_operation = models.CharField(max_length=200,verbose_name="le nom de l'operation",blank=True,unique=True)
    date_operation = models.DateField(verbose_name="la date de l'operation")
    agent_fk = models.ManyToManyField(Agent,verbose_name="les agents")
    nombre_des_agents = models.IntegerField(verbose_name="le nombres des agents")
    nombre_des_migrants = models.IntegerField(verbose_name="le nombres des migrants")
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commissariat = models.ForeignKey(Commissariat_De_Police,on_delete=models.CASCADE)

    def __str__(self) :
        return 'Le {} à {}'.format(self.date_operation,self.region)



