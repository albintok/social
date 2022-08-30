from django.db import models

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="postImages",null=True)
    user=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)