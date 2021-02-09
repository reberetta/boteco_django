from django.contrib import admin
from team.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'descrition')
    
admin.site.register(Team, TeamAdmin)
