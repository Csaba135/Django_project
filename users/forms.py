from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from users.models import Customer
from django.forms.widgets import DateInput

AuthUser = get_user_model()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['email']

    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html
    )
    password_confirmation = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data['password']

        user = AuthUser(
            email=email
        )
        validate_password(password, user=user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password not confirmed.')

        return password_confirmation

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit is True:
            user.save()

        return user

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['date_of_birth', 'nationality', 'age']
        labels = {
            'date_of_birth': ('Date Of Birth'),
        }
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

class RegisterFirstLastName(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name']
