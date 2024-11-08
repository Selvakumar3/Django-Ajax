from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.DateField()
    gender=models.CharField(max_length=50)
    degree=models.TextField(max_length=50)
    address=models.TextField(max_length=255)
    
    
    def __str__(self):
        return self.name
