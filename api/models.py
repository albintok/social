from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

class Posts(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    image=models.ImageField(null=True,upload_to="imageupload")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class comments(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    user=models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.comment

# Create your models here.
=======

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="postImages",null=True)
    user=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
>>>>>>> 21a118e6ed0caa28520a683f6e8b2e4c24bfd597
