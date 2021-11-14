from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=30ff1f905d234ce84fc94bc5634f340f'  
    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()

    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()

        weather_dict = {
          'cityname': city,
          'temp': r['main']['temp'],
          'desc': r['weather'][0]['description'],
          'icon': r['weather'][0]['icon'],
        }
        weather_data.append(weather_dict)

    context = {
        'weather_data': weather_data,
        'form': form
    }
    return render(request, 'index.html', context)