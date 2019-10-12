from django import forms

class PatientForm(forms.Form):
    PATIENT_STATUS = (
        ('ACT', 'ACT'),
        ('RIP', 'RIP'),
        ('MIA', 'MIA'),
    )
    name = forms.CharField(max_length=100, label='Patient Name')
    identity_card = forms.CharField(max_length=12, primary_key=True)
    address = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    transfer = forms.CharField(max_length=100, default='Not transferred')
    patient_number = forms.CharField(max_length=12, label='Patient Number')
    patient_status = forms.CharField(
        max_length=3,
        choices=PATIENT_STATUS,
        blank=True,
        default='ACT',
        help_text='Patient status',
        )
    time_registered = forms.DateTimeField()