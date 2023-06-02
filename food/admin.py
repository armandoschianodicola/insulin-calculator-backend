from django.contrib import admin
from django.contrib import admin
from . import models


class RecipeAdmin(admin.ModelAdmin):
    model = models.Food
    readonly_fields = ['created', 'modified']


# Register your models here.
admin.site.register(models.Food)
