from django.contrib import admin
from .models import Account
# Register your models here.

@admin.register(Account)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'account_number', 
                    'account_serial', 'account_date_creation']
    
    search_fields = ['account_name']