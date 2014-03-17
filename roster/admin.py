from django.contrib import admin
from roster.models import Player
from roster.models import Coach
from roster.models import Team

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
class CoachAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Team, TeamAdmin)