from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .models import Profile, PtoHistory
User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    # Add an additional email field in the form but not the model for error/form handling.
    confirm_email = forms.EmailField(label='Confirm Email')
    # Mask the password while the user is typing.
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # Model to be used in the form
        model = User
        # Determine fields to include from the model and the order in which the form inputs will be displayed
        fields = [
            'email',
            'confirm_email',
            'username',
            'password',
        ]
    # Function runs on submit.  Checks form for errors.
    def clean_confirm_email(self):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email != confirm_email:
            raise forms.ValidationError('Emails must match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email has already been registered')
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        # Model to be used in the form.
        model = Profile
        # Define which model fields to include in the form.
        fields = ('pto_tier',)


class UserLoginForm(forms.Form):
    # Define form fields to include.
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # Check if user exists and logs in.
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or password is incorrect.')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class PtoRequestForm(forms.ModelForm):
    class Meta:
        # Model to be used in the form.
        model = PtoHistory
        # Define which model fields to include in the form.
        fields = [
            'start',
            'end',
            'leave_type',
        ]
        # Attach input widgets to fields for a friendlier user interface.
        widgets = {
            'start': DateTimeWidget(attrs={'id':'start'}, usel10n = True, bootstrap_version=3),
            'end': DateTimeWidget(attrs={'id':'end'}, usel10n = True, bootstrap_version=3),
        }
