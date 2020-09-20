from django.db import models

# Create your models here.
class User(models.Model):
    slackID = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Snack(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)
    timestamp = models.TimeField

    def __str__(self):
        return self.user.__str__()
