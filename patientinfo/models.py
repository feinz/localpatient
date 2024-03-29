from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.    

class Patient(models.Model):
    
    """Model representing a patient details."""
    PATIENT_STATUS = (
        ('Active', 'Active'),
        ('Rest In Peace', 'Rest In Peace'),
        ('Missing', 'Missing'),
    )

    name = models.CharField(max_length=100)
    identity_card_number = models.CharField(max_length=12, primary_key=True, validators=[RegexValidator(r'^\d{12,12}$')])
    # address = models.CharField(max_length=200)
    # description = models.CharField(max_length=200)
    transfer = models.CharField(max_length=100, default='Not Transferred')
    # patient_number = models.CharField(max_length=12)
    patient_status = models.CharField(
        max_length=20,
        choices=PATIENT_STATUS,
        blank=True,
        default='Active',
        )
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    time_registered = models.DateTimeField(help_text='Pick Patient Register Time In Hospital',null=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """String for representing the Model object."""
        #to return who is the data belongs to
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this patient."""
        # ic is the primary key for patient
        return reverse('patient_detail', args=[str(self.identity_card_number)])
