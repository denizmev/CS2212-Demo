from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
