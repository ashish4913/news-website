from django.db import models


# Create your models here.
class subcategory(models.Model):
    subcat=models.CharField(max_length=20) #football
    catname=models.CharField(max_length=20)#sports
    catid=models.IntegerField()

    def __str__(self):
        return self.subcat
