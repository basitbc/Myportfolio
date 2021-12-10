from django import forms
from . import models


from django import forms
from . import models


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'Subject'}))
    message = forms.CharField(max_length=264, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20, 'placeholder': 'Write your message'}))

    class Meta:
        fields = ('name', 'email', 'subject', 'message')
        model = models.Contact
