from django.contrib import admin
from sport.models import Sport

class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Sport, SportAdmin)
