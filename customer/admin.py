from django.contrib import admin
from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'phone')

admin.site.register(Customer, CustomerAdmin)
