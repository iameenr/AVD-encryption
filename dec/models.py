from django.db import models

# Create your models here.


class DecKey(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.TextField()
    r_seq = models.TextField()
    keys = models.TextField()

    def save(self, *args, **kwargs):
        super(DecKey, self).save()

    def __str__(self):
        return "DecKey {}".format(id)
