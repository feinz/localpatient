from django.contrib import admin

# Register your models here.

from catalog.models import Patient

# admin.site.register(patient)
@admin.register(Patient)
class patientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name','ic','address')
        }),
        ('Hospital Information', {
            'fields': ('description','transfer','patientnumber','patientstatus')
        }),
    )
    list_display = ('name','ic','address','description','transfer','patientnumber','patientstatus')
    list_filter = ('patientstatus',)
    # fields = ['name','ic','description','transfer','patientnumber','patientstatus']