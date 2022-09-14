from django.db import models
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
