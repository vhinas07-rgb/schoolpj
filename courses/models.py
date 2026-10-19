from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
   
    def __str__(self):
        return self.name
   
   
   
class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    duration = models.CharField(max_length=100)
   
   
   
    def __str__(self):
        return self.title
 

