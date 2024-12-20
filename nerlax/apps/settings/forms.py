from django import forms
from .models import *


class SupplierForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['city'].queryset = City.objects.filter(
                    state=region_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.region.city_set.order_by('name')

    class Meta:
        model = Supplier
        fields = ['name', 'nro_documento', 'logo', 'address', 'address2', 'city',
                  'postal_code', 'region', 'mobile', 'email', ]
        labels = {
            'name': "Name",
            'nro_documento': "Nro documento",
            'address': "Address",
            'address2': "Address2",
            'city': "City",
            'postal_code': "Postal code",
            'region': "Region",
            'mobile': "Mobile",
            'email': "Email",
            'logo': "Upload Image"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control',
                }),
            'address': forms.TextInput(
                attrs={
                    'id': 'address',
                    'placeholder': 'Street address',
                    'class': 'form-control',
                }),
            'address2': forms.TextInput(
                attrs={
                    'placeholder': 'Street addres line 2',
                    'id': 'address2',
                    'class': 'form-control',
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code',
                    'class': 'form-control',
                }),
            'mobile': forms.TextInput(
                attrs={
                    'id': 'mobile',
                    'class': 'form-control',
                }),
            'nro_documento': forms.TextInput(
                attrs={
                    'id': 'nro_documento',
                    'class': 'form-control',
                }),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'class': 'form-control',
                }),
        }


class ActivityTypeForm(forms.ModelForm):
    class Meta:
        model = ActivityType
        fields = ['name', 'description']
        labels = {
            'name': "Name",
            'description': "Description"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                })
        }


class ClassificationForm(forms.ModelForm):
    class Meta:
        model = Classification
        fields = ['name', 'description']
        labels = {
            'name': "Name",
            'description': "Description"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                })
        }


class ServicesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.filter(state=True)

    class Meta:
        model = Services
        fields = ['name', 'supplier']
        labels = {
            'name': 'Name',
            'supplier': 'Supplier'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control mb-3',
                }),
        }


class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ['name', 'code']
        labels = {
            'name': 'State',
            'code': 'Code'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control'
                }),
            'code': forms.TextInput(
                attrs={
                    'id': 'code',
                    'class': 'form-control'
                }),
        }


class CityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.filter(active=True)

    class Meta:
        model = City
        fields = ['name', 'state', 'code']
        labels = {
            'name': 'City',
            'state': 'State',
            'code': 'Code'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control'
                }),
            'code': forms.TextInput(
                attrs={
                    'id': 'code',
                    'class': 'form-control'
                }),
        }
