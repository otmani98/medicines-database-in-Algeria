from django.contrib import admin

from .models import MedicinesModel


# Register your models here.
class MedicinesAdmin(admin.ModelAdmin) :
    list_filter = ("laboratories","country")
    list_display = ("registration_no", "code", "inn", "bn", "form", "dosing", "cond", "list", "p1", "p2", "laboratories","country")

admin.site.register(MedicinesModel, MedicinesAdmin)