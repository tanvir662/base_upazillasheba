from django.db import models
# Create your models here.

class Generalpeople(models.Model):
    name = models.CharField(max_length= 200)
    phone= models.IntegerField()
    district = models.CharField(max_length=100)
    upozilla = models.CharField(max_length=100)
    union = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Complain(models.Model):

    catagory = models.CharField(max_length= 100)
    complain = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')
    gp_id=models.ForeignKey(Generalpeople,on_delete=models.CASCADE)
    assignCom = models.BooleanField(default=False)
    def __int__(self):
        return self.id
