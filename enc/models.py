from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()
    account_number = models.BigIntegerField()
    odec = models.AutoField(primary_key=True)
    aadhar_number = models.TextField()
    current_balance = models.TextField()

    def save(self, *args, **kwargs):
        super(User, self).save()

    def __str__(self):
        return self.username
