from django.db import models


class Artiste(models.Model):
    nom = models.CharField(max_length=64)

    def __str__(self):
        return self.nom

class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE, null=False)
    date_sortie = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.titre} ({self.artiste})'
    
    

