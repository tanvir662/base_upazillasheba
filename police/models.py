from django.db import models

# Create your models here.
class Police(models.Model):
    policeId=models.AutoField(primary_key=True)
    username =models.CharField(max_length=100 ,blank=False,null=False )
    password=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.username