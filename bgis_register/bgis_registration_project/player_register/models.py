from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)


class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)    

    def __str__(self):
        return self.name
