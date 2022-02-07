from django.db import models

# Create your models here.


class Administrators(models.Model):
    name = models.CharField(max_length=20)
    password = models.TextField()

    def __str__(self):
        return "{}".format(self.name)
