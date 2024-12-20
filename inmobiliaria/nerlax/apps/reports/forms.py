from django.forms import *
from ..building.models import Unit


class CeReportForm(Form):
    date_report = DateField(
        label='Date',
        widget=DateInput(attrs={
            'placeholder': 'dd/mm/aaaa',
            'id': 'report_date',
            'class': 'form-control',
        }))
    apartment = ModelChoiceField(label='Apartment', queryset=Unit.objects.all())
