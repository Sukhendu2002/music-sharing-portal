from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import CustomUser
from .models import File


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']


class UploadForm(forms.ModelForm):
    file_name = forms.CharField(max_length=255, required=True)
    file_status = forms.ChoiceField(
        choices=File.FILE_STATUS_CHOICES, required=True)
    allowed_emails = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'email-input'}))

    class Meta:
        model = File
        fields = ['file_name', 'audio_file', 'file_status', 'allowed_emails']

    def clean_allowed_emails(self):
        file_status = self.cleaned_data.get('file_status')
        allowed_emails = self.cleaned_data.get('allowed_emails')

        if file_status == 'protected':
            email_list = allowed_emails.split(',')
            cleaned_emails = []

            for email in email_list:
                email = email.strip()

                try:
                    validate_email(email)
                    cleaned_emails.append(email)
                except forms.ValidationError:
                    raise forms.ValidationError(
                        f"Invalid email address: {email}")

            return cleaned_emails

        return []

    def clean(self):
        cleaned_data = super().clean()
        file_status = cleaned_data.get('file_status')
        allowed_emails = cleaned_data.get('allowed_emails')

        if file_status == 'protected' and not allowed_emails:
            raise forms.ValidationError(
                "Please provide at least one email address for protected files.")

        return cleaned_data


class UpdateFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_name', 'file_status', 'allowed_emails']
        widgets = {
            'allowed_emails': forms.TextInput(attrs={'placeholder': 'Enter emails separated by commas'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Allow the field to be optional
        self.fields['allowed_emails'].required = False
