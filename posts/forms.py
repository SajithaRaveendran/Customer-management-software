from django import forms
from django.forms import TextInput, Select, DateInput, BooleanField,Textarea

from posts.models import Customer,Event


class CustomerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "input","type": "text"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': "input","type": "password"}))
    class Meta:
        model = Customer
        exclude = ('user', 'is_deleted')

        widgets = {
            'phone_no': TextInput(attrs={'class': "input","type": "text"}),
            'name': TextInput(attrs={'class': "input","type": "text"}),
            'email': TextInput(attrs={'class': "input","type": "text"}),
            'address': Textarea(attrs={'class': "input", 'rows':5,"type": "text"}),
            'date_of_birth': DateInput(attrs={"type": "date", 'style':"background:#fff;color:#000"}),
            
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={'class':'required input'}),
            'event_type': Select(attrs={'class':'required input'},choices=Event.CHOICES),
            'event_date': DateInput(attrs={'class':'required input', 'type':'date'}, format="%Y-%m-%dT%H:%M"),
        }
        
