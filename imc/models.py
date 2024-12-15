from django.db import models

class Person(models.Model):
    user = models.CharField(max_length=50,unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    poids = models.IntegerField(default=0)
    taille = models.IntegerField(default=0)
    date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user + " " + self.nom
    
   