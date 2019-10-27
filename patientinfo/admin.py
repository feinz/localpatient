from django.contrib import admin

# Register your models here.

from patientinfo.models import Patient

# admin.site.register(patient)
@admin.register(Patient)
class patientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name','identity_card_number','address')
        }),
        ('Hospital Information', {
            'fields': ('transfer','patient_status')
        }),
        ('System Information', {
            'fields': ('time_created','time_modified')
        }),
    )
    list_display = ('name','identity_card_number','transfer','patient_status')
    list_filter = ('patient_status',)
    # fields = ['name','ic','description','transfer','patientnumber','patientstatus']