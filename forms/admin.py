from django.contrib import admin

from forms import models


@admin.register(models.Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'voximplant_id', 'is_active')


@admin.register(models.TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('time', 'contract')