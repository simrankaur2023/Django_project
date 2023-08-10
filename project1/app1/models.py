from django.db import models

# Create your models here.
class students(models.Model):
    name = models.TextField(max_length =20)
    roll_no = models.IntegerField(primary_key=True)
    d_o_ad = models.DateField(auto_now_add= True)
class classroom(models.Model):
    classroom = models.IntegerField(primary_key=True)
    class_teacher = models.TextField(max_length =20)    
class teacher(models.Model):
    ID_no = models.IntegerField(primary_key = True)
    name = models.TextField(max_length = 20)
class marks(models.Model):
    subject = models.TextField(max_length =20)
    marks = models.IntegerField(primary_key = True) 