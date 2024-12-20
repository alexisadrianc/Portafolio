from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from .models import *

CUSTOMER = '1'
EMPLOYEE = '2'
USER_TYPE = (
    (CUSTOMER, 'CUSTOMER'),
    (EMPLOYEE, 'EMPLOYEE'),
)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Username',
                    'name': 'username'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Password',
                    'name': 'pass'
                }),
        }


class RegisterUserForm(UserCreationForm):
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input--style-4',
            'id': 'password2',
        }
    ))

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'user_type']
        labels = {
            'username': 'User',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password': 'Password',
            'email': 'Email',
            'user_type': 'User type'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'username'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'first_name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'last_name'
                }),
            'email': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'password'
                }),

        }


class UsersForm(forms.ModelForm):
    """Adding new field password for validate password of the new user"""
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password2',
            'required': 'required',
            'placeholder': 'Confirm password',
        }
    ))

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'user_type', 'company', 'image']
        labels = {
            'username': 'User',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password': 'Password',
            'email': 'Email',
            'user_type': 'User type',
            'company': 'Company',
            'image': 'Image',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'username'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First name',
                    'id': 'first_name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last name',
                    'id': 'last_name'
                }),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'id': 'email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'name': 'password'
                }),
            'user_type': forms.Select(
                choices=USER_TYPE,
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def clean_password2(self):
        """ Validation pass method for validate password """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("The passwords are not equals ")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'rut_dgi', 'address', 'address2', 'city', 'postal_code',
                  'region', 'mobile', 'email', 'image']
        labels = {
            'name': "Name",
            'rut_dgi': "RUT DGI",
            'address': "Address",
            'address2': "Address2",
            'city': "City",
            'postal_code': "Postal code",
            'region': "Zone",
            'mobile': "Mobile",
            'email': "Email",
            'image': 'Logo'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'address',
                    'placeholder': 'Street address'
                }),
            'address2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street addres line 2',
                    'id': 'address2',
                }),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'city',
                    'placeholder': 'City'
                }),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'region',
                    'placeholder': 'Zone'
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code'
                }),
            'mobile': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'mobile'
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email'
                }),
            'rut_dgi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'RUT',
                    'id': 'rut_dgi'
                }),
        }


class RolesForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['name',]
        labels = {
            'name': "Name",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Group name ...',
                    'id': 'name',
                    'class': 'form-control',
                }),
        }
