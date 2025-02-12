from django import forms


# Form for the contact
class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Subject", required=True)
    message = forms.CharField(label="Message", widget=forms.Textarea, required=True)

