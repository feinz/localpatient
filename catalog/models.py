from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.

class status(models.Model):
    """Model representing patient's status."""
    PATIENT_STATUS = (
        ('a', 'Active'),
        ('r', 'RIP'),
        ('m', 'MIA'),
    )
    patientstatus = models.CharField(
        max_length=1,
        choices=PATIENT_STATUS,
        blank=True,
        default='a',
        help_text='Patient status',
        )
    
    def __str__(self):
        """String for representing the Model object."""
        return self.patientstatus

class patient(models.Model):
    """Model representing a patient details."""
    name = models.CharField(max_length=200)
    ic = models.CharField(max_length=12)
    address = models.TextField
    description = models.TextField
    transfer = models.CharField(max_length=200, default='Not transferred')
    patientnumber = models.CharField(max_length=12)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this patient."""
        return reverse('book-detail', args=[str(self.id)])