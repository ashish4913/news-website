from django.db import models

# Create your models here.
class main(models.Model):
    title=models.CharField(max_length=20)
    about=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Trandingpost(models.Model):
    about=models.CharField(max_length=10)
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    img = models.ImageField(upload_to='news', default="")
    imgname=models.CharField(max_length=50,default="-")
    details=models.TextField(max_length=500000,default="-")
    writer=models.CharField(max_length=50,default="Ashish")
    views=models.IntegerField(default=0)
    def __str__(self):
         return self.about