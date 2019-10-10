from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.    

class Patient(models.Model):
    
    """Model representing a patient details."""
    PATIENT_STATUS = (
        ('ACT', 'ACT'),
        ('RIP', 'RIP'),
        ('MIA', 'MIA'),
    )

    name = models.CharField(max_length=200)
    identity_card = models.CharField(max_length=12, primary_key=True)
    address = models.TextField()
    description = models.TextField()
    transfer = models.CharField(max_length=200, default='Not transferred')
    patient_number = models.CharField(max_length=12)
    patient_status = models.CharField(
        max_length=3,
        choices=PATIENT_STATUS,
        blank=True,
        default='ACT',
        help_text='Patient status',
        )

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """String for representing the Model object."""
        #to return who is the data belongs to
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this patient."""
        # ic is the primary key for patient
        return reverse('patient_detail', args=[str(self.identity_card)])