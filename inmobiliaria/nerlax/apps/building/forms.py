from django import forms
from .models import *


class buildingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(buildingForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.filter(state=True)
        self.fields['type_resource'].queryset = Classification.objects.filter(state=True)
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
        model = Building
        fields = ['name', 'address', 'address2', 'city', 'postal_code', 'supplier',
                  'region', 'unit_qty', 'amenities', 'type_resource', 'description']
        labels = {
            'name': 'Name',
            'address': 'Address',
            'unit_qty': 'Quantity of flat',
            'amenities': 'Has it amenities ?',
            'type_resource': 'Property type',
            'supplier': 'Supplier',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Building name ...',
                    'id': 'name',
                    'class': 'form-control',
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street address'
                }),
            'address2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street addres line 2'
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code',
                    'class': 'form-control',
                }),
            'amenities': forms.CheckboxInput(
                attrs={
                    'id': 'aminities',
                    'class': 'form-check-input',
                }),
            'unit_qty': forms.NumberInput(
                attrs={
                    'id': 'unit_qty',
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                }),
            'supplier': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                })
        }


class unitForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(unitForm, self).__init__(*args, **kwargs)
        self.fields['renter'].queryset = UserModel.objects.filter(is_active=True)
        self.fields['building_id'].queryset = Building.objects.filter(state=True)
        self.fields['type_resource'].queryset = Classification.objects.filter(state=True)

    class Meta:
        model = Unit
        fields = ['number', 'meter_qty', 'flat', 'rent_price', 'renter',
                  'init_date', 'name', 'type_resource', 'building_id', 'garage',
                  'renovation_date', 'expiration_date', 'description']
        labels = {
            'name': 'Name',
            'init_date': 'Contract start date',
            'number': 'Number of unit',
            'meter_qty': 'M2',
            'rent_price': 'Price of rent',
            'expiration_date': 'Contract expiration date',
            'renovation_date': 'Contract renovation date',
            'renter': 'Renter',
            'building_id': 'Building',
            'garage': 'Has it garage ?',
            'type_resource': 'Property type',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Unit name ...',
                    'id': 'name',
                    'class': 'form-control',
                }),
            'init_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'id': 'init_date',
                    'class': 'form-control',
                }),
            'number': forms.TextInput(
                attrs={
                    'placeholder': 'Unit ...',
                    'class': 'form-control',
                    'id': 'number'

                }),
            'flat': forms.TextInput(
                attrs={
                    'placeholder': 'Flat ...',
                    'class': 'form-control',
                    'id': 'flat'
                }),
            'meter_qty': forms.NumberInput(
                attrs={
                    'id': 'meter_qty',
                    'class': 'form-control',
                }),
            'garage': forms.CheckboxInput(
                attrs={
                    'id': 'garage',
                    'class': 'form-check-input',
                }),
            'rent_price': forms.NumberInput(
                attrs={
                    'id': 'rent_price',
                    'class': 'form-control',
                }),
            'expiration_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'id': 'expiration_date',
                    'class': 'form-control',
                }),
            'renovation_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'id': 'renovation_date',
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                }),

        }


class commonExpensesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(commonExpensesForm, self).__init__(*args, **kwargs)
        self.fields['building'].queryset = Building.objects.filter(state=True)

    class Meta:
        model = CommonExpenses
        fields = ['building', 'payment_date', 'total_amount']
        labels = {
            'building': 'Building',
            'payment_date': 'Payment date',
            'total_amount': 'Amount',
        }
        widgets = {
            'payment_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'form-control',
                    'id': 'payment_date'
                }),
            'total_amount': forms.NumberInput(
                attrs={
                    'id': 'total_amount',
                    'class': 'form-control',
                }),
        }


class commonExpensesLinesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(commonExpensesLinesForm, self).__init__(*args, **kwargs)
        self.fields['concept'].queryset = Services.objects.filter(state=True)

    class Meta:
        model = CommonExpensesLines
        fields = ['concept', 'amount', 'common_expenses']
        labels = {
            'concept': 'Concept',
            'common_expenses': 'Concept expenses',
            'amount': 'Amount',
        }
        widgets = {
            'amount': forms.NumberInput(
                attrs={
                    'id': 'amount',
                    'class': 'form-control',
                }),
        }


class GarageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GarageForm, self).__init__(*args, **kwargs)
        self.fields['building'].queryset = Building.objects.filter(state=True)

    class Meta:
        model = Garage
        fields = ['name', 'total_amount', 'building', 'payment_date']
        labels = {
            'name': 'Name',
            'building': 'Building',
            'total_amount': 'Amount',
            'payment_date': 'Date',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name ...',
                    'id': 'name',
                    'class': 'form-control',
                }),
            'total_amount': forms.NumberInput(
                attrs={
                    'id': 'total_amount',
                    'class': 'form-control',
                }),
            'payment_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'form-control',
                    'id': 'payment_date_g'
                }),
        }

    # def clean_building(self):
    #     building = self.cleaned_data.get('building')
    #     date = self.cleaned_data.get('payment_date')
    #     if building != "":
    #         if date != "":
    #             for instance in Garage.objects.all():
    #                 if instance.building == building:
    #                     raise forms.ValidationError("There is a garage with this building"+building+"and this date"+date)
    #         return building
    #     raise forms.ValidationError("This field cannot be left blank")
    #
    # def clean_payment_date(self):
    #     payment_date = self.cleaned_data.get('payment_date')
    #     building = self.cleaned_data.get('building')
    #     if payment_date != "":
    #         if building != "":
    #             for instance in Garage.objects.all():
    #                 if instance.building == building:
    #                     raise forms.ValidationError(
    #                         "There is a garage with this building" + building + "and this date" + payment_date)
    #         return payment_date
    #     raise forms.ValidationError("This field cannot be left blank")
    #
    # def clean_total_amount(self):
    #     amount = self.cleaned_data.get('total_amount')
    #     if amount > 0:
    #         return amount
    #     raise forms.ValidationError("The value can not be less than 0 ")


class GarageLinesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GarageLinesForm, self).__init__(*args, **kwargs)
        self.fields['garage'].queryset = Garage.objects.filter(state=True)
        self.fields['apartment'].queryset = Unit.objects.filter(state=True)

    class Meta:
        model = GarageLines
        fields = ['amount', 'apartment', 'is_paid', 'voucher', 'garage']
        labels = {
            'amount': 'Amount',
            'apartment': 'Apartment',
            'is_paid': 'Is paid',
            'voucher': 'Voucher',
            'garage': 'Garage'
        }
        widgets = {
            'amount': forms.NumberInput(
                attrs={
                    'id': 'total_amount',
                    'class': 'form-control',
                }),
        }
