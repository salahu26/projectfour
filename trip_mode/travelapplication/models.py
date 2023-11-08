from django.db import models


# Create your models here.
class picture(models.Model):
    name= models.CharField(max_length=222)
    image= models.ImageField(upload_to='pics')     # the name "pics" be created in the left side as folder
    desc=models.TextField()




    def __str__(self):
        return self.name

class my_team(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='pho')
    detalis=models.TextField()
    id_num=models.IntegerField()


    def __str__(self):
        return self.name