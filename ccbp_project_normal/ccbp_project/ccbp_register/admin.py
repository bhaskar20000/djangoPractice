from django.contrib import admin
from .models import Player , Role   
# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display=["name" , "age" , "team"]
    list_filter = ("age",)
    list_display_links = ("name",)
    list_per_page = 1 
    readonly_fields = ("team",)
    list_editable = ("age",)
    





admin.site.register(Player , PlayerAdmin)
admin.site.register(Role)
