from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, help_text='Require.')
    email = forms.EmailField(max_length=255, help_text='Require. Inform a valid email address.')
    phone = forms.CharField(max_length=11, help_text='Required.')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text='Your password can\'t be too similar to your other personal information.'
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput,
        help_text='Enter the same password as before, for verification.'
    )
    
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone','password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data('email')
        user.first_name = self.cleaned_data['full_name'].split(' ')[0]
        user.last_name = self.cleaned_data['full_name'].split(' ')[1] if ' ' in self.cleaned_data['full_name'] else ''
        if commit:
            user.save()
        return user