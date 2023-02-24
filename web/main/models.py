from django.db import models

# Create your models here.
class temata(models.Model):
    tema = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tema

class druh(models.Model):
    temata = models.ForeignKey(temata, on_delete=models.CASCADE)
    jmeno = models.CharField(max_length=200)
    text =  models.CharField(max_length=500)