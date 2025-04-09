from .models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Account
        fields = ['account_name', 'account_number',
                   'account_serial', 'account_date_creation']