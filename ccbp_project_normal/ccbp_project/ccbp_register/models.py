from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.name   
    

class Role(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name