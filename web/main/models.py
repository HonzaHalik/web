from django.db import models

# Create your models here.
class Temata(models.Model):
    jmeno = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tema

class Druh(models.Model):
    temata = models.ForeignKey(Temata, on_delete=models.CASCADE)
    jmeno = models.CharField(max_length=200)
    text =  models.CharField(max_length=500)