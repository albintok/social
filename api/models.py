from django.db import models

class Posts(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    image=models.ImageField(null=True,upload_to="imageupload")
    user=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
