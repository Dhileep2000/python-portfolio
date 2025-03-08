from django.db import models

class model_port(models.Model):

    name=models.CharField( max_length=50,null=True)
    email=models.EmailField( max_length=254,null=True)
    phonenumber=models.IntegerField(default=0)
    message=models.CharField( max_length=250)

    def __str__(self):
        return self.name
    

