from django.db import models





class Province(models.Model) :
    nom_province = models.CharField(max_length=50)

    def __str__(self) :
        return self.nom_province






class Region(models.Model) :
    nom_region = models.CharField(max_length=50)

    def __str__(self) :
        return self.nom_region







class Commissariat_De_Police(models.Model) :
    nom_commissariat = models.CharField(max_length=50)

    def __str__(self) :
        return self.nom_commissariat






class Lieu_De_Travail(models.Model) :
    
    region_fk = models.OneToOneField(Region,on_delete=models.CASCADE)
    province_fk = models.OneToOneField(Province,on_delete=models.CASCADE)
    commissariat_fk = models.OneToOneField(Commissariat_De_Police, on_delete=models.CASCADE)


    def __str__(self) :
        return '{} {} {}'.format(self.commissariat_fk,self.province_fk,self.region_fk)


