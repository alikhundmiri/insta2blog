from django import forms
from django.core.validators import validate_email

from .models import newsletter_list

# Form for "newsletter_list"
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter_list
        fields = [
        'email_address',
        ]

    def clean_contact(self):
        this_email = self.cleaned_data.get('email_address')
        try:
            validate_email(this_email)
        except forms.ValidationError:
            raise forms.ValidationError("Please enter a Valid Email address")

        existing_email = newsletter_list.objects.filter(email_address=this_email)

        if existing_contact:
            print("CONFLICT OF EMAILS")
            raise forms.ValidationError("You already submitted a request with these credentials")
        else:
            print("NO CONFLICT FOUND")
            return this_email

    def __init__(self, *args , **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields["email_address"].help_text = "Please expect our email with in 24 hours."
        self.fields["email_address"].label = "Your Email Addresss"
