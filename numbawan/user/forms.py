from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=255, help_text="Require.")
    email = forms.EmailField(
        max_length=255, help_text="Require. Inform a valid email address."
    )
    phone = forms.CharField(
        validators=[MinLengthValidator(11), MaxLengthValidator(11)],
        help_text="Required. Must be exactly 11 numbers.",
    )
    birthday = forms.DateField(help_text="Require.")
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Your password can't be too similar to your other personal information.",
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ["name", "email", "birthday", "phone", "password1", "password2"]

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if len(phone) != 11:
                raise forms.ValidationError(
                    "Phone number must be exactly 11 characters long."
                )
            try:
                return int(phone)
            except ValueError:
                raise forms.ValidationError(
                    "Phone number must be a number not characters."
                )
        return int(phone)

    def save(self, commit=True):
        user = super().save(commit=False)

        if not user.username:
            user.username = self.cleaned_data["email"].split("@")[0]
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        user.first_name = self.cleaned_data["name"].split(" ")[0]
        user.last_name = (
            self.cleaned_data["name"].split(" ")[1]
            if " " in self.cleaned_data["name"]
            else ""
        )
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='email')
    password = forms.CharField(widget=forms.PasswordInput)