from django.contrib import admin

# Register your models here.

from catalog.models import Patient

# admin.site.register(patient)
@admin.register(Patient)
class patientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name','identity_card','address')
        }),
        ('Hospital Information', {
            'fields': ('description','transfer','patient_number','patient_status')
        }),
        ('System Information', {
            'fields': ('time_created','time_modified')
        }),
    )
    list_display = ('name','identity_card','address','description','transfer','patient_number','patient_status')
    list_filter = ('patient_status',)
    # fields = ['name','ic','description','transfer','patientnumber','patientstatus']