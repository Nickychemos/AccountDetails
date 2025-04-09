from django.db import models
from django.utils import timezone

# Create your models here.

class Account(models.Model):
    class Meta:
        verbose_name_plural = 'Accounts'
    
    account_name = models.CharField(max_length=200, null=False, blank=False)
    account_number = models.CharField(max_length=100, null=False, blank = False)
    account_serial = models.CharField(max_length=100)
    account_date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.account_serial}'
    