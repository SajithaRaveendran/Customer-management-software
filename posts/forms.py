from django import forms
from django.forms import TextInput, Select, DateInput, BooleanField

from posts.models import Customer,Event


class CustomerForm(forms.ModelForm):
    event = forms.CharField(widget=forms.TextInput(
        attrs={'class': "input"}))
    phone_no = forms.CharField(widget=forms.TextInput(
        attrs={'class': "input","type": "number"}))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': "input"}))
    event_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': "date",'class':"input"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={'type': "date",'class':"input"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'type': "email",'class':"input","placeholder": "Enter Your Email Address"}))
    
    class Meta:
        model = Customer
        exclude = ('customer', 'is_deleted')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={'class':'required input'}),
            'event_type': Select(attrs={'class':'required input'},choices=Event.CHOICES),
            'event_date': DateInput(attrs={'class':'required input', 'type':'date'}, format="%Y-%m-%dT%H:%M"),
        }
        
