from django.contrib import admin
from .models import Pharmacy

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'address', 'phone', 'work_mode')
    list_filter = ('work_mode',)
    search_fields = ('number', 'name', 'address')
