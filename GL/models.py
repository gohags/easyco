from django.db import models

# Create your models here.
class Account(models.Model):
    AccountName = models.CharField(max_length=250)
    AccountNumber = models.CharField(max_length=20)
    BalanceType = models.CharField(max_length=20)
    Balance =  models.FloatField(default=0)

    def __str__(self):
          return self.AccountName