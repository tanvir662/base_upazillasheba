from django.db import models

# Create your models here.
from calc.models import Complain
from chairman.models import Chairman
from police.models import Police
from uno.models import Uno


class AssignComplainPolice(models.Model):
    complainId = models.AutoField(primary_key=True)
    police=models.ForeignKey(Police,on_delete=models.CASCADE)
    complain=models.ForeignKey(Complain,on_delete=models.CASCADE)
    setmeetingdate = models.CharField(max_length=25,null=True)
    setmeetingtime = models.CharField(max_length=25,null=True)
    status=models.CharField(max_length=25,null=True)

    def __str__(self):
        return self.police.username

class AssignComplainChairman(models.Model):
    complainId = models.AutoField(primary_key=True)
    chairman = models.ForeignKey(Chairman, on_delete=models.CASCADE)
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    setmeetingdate = models.CharField(max_length=25,null=True)
    setmeetingtime = models.CharField(max_length=25,null=True)
    status = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.chairman.username

class AssignComplainUno(models.Model):
    complainId = models.AutoField(primary_key=True)
    uno = models.ForeignKey(Uno, on_delete=models.CASCADE)
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE )
    setmeetingdate = models.CharField(max_length=25,null=True)
    setmeetingtime = models.CharField(max_length=25,null=True)
    status = models.CharField(max_length=25, null=True)

    def __str__(self):
      return self.uno.username