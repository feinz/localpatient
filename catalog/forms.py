from django import forms

class PatientForm(forms.Form):
    PATIENT_STATUS = (
        ('ACT', 'ACT'),
        ('RIP', 'RIP'),
        ('MIA', 'MIA'),
    )
    name = forms.CharField(max_length=200)
    ic = forms.CharField(max_length=12, primary_key=True)
    address = forms.CharField()
    description = forms.CharField()
    transfer = forms.CharField(max_length=200, default='Not transferred')
    patientnumber = forms.CharField(max_length=12)
    patientstatus = forms.CharField(
        max_length=3,
        choices=PATIENT_STATUS,
        blank=True,
        default='ACT',
        help_text='Patient status',
        )

