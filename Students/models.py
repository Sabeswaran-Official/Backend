from django.db import models

# Create your models here.

'''
class SampleTable(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    weight=models.FloatField(null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    D_O_B=models.DateField(auto_now=True)
    Birth_time=models.TimeField(auto_now=True)

    is_admin=models.BooleanField(default=False)
    feedback=models.TextField(max_length=100,null=True)
'''

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    d_o_b=models.DateField(auto_now=False)
    place=models.CharField(max_length=20)
    admin=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Task(models.Model):

    student_reference=models.ForeignKey(Student,related_name='all_task',on_delete=models.CASCADE,null=True)

    task_name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.task_name
    
class RankSheet(models.Model):
    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social_science=models.IntegerField()
    total=models.IntegerField()
    average=models.FloatField()
    result=models.BooleanField()