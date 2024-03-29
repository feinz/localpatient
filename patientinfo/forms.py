from django import forms
MY_DATE_FORMATS = ['%d/%m/%Y',]

class PatientForm(forms.Form):
    PATIENT_STATUS = ( 
        ('Active', 'Active'),
        ('Rest In Peace', 'Rest In Peace'),
        ('Missing', 'Missing'),
    )
    name = forms.CharField(max_length=100, label='Patient Name')
    identity_card_number = forms.CharField(max_length=12, primary_key=True)
    # address = forms.CharField(max_length=100)
    # description = forms.CharField(max_length=100)
    transfer = forms.CharField(max_length=100, default='Not transferred')
    # patient_number = forms.CharField(max_length=12, label='Patient Number')
    patient_status = forms.ChoiceField(
        max_length=20,
        choices=PATIENT_STATUS,
        blank=True,
        default='Active',
        )
    time_registered = forms.DateTimeField(input_formats=MY_DATE_FORMATS)