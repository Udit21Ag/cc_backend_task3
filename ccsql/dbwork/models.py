from django.db import models

# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=200)
    data=models.BinaryField()

    def __str__(self):
        return self.name