from .models import City
from django.forms import ModelForm, TextInput, fields, widgets
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class':'input', 'placeholder': 'cityname' })}
    
