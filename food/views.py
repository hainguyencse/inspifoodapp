from inspifoodapp import settings
import urllib, json
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    url = settings.INSPIFOOD_API + "foodgroups/"
    data = urllib.urlopen(url)
    data = json.loads(data.read())
    foodgroups = data['results']

    response = []
    for group in foodgroups:
        response.append({
            "label": group['name'],
            "value": 1,
            "question": "Do you want to eat " + group['name'] + "?",
            "slug": group['slug']
        })

    return render(request, 'main/index.html', {'response': json.dumps(response)})


def detail(request, foodgroups):
    url = settings.INSPIFOOD_API + "foods/" + "?food_group=" + foodgroups
    data = urllib.urlopen(url)
    data = json.loads(data.read())
    foods = data['results']

    return render(request, 'main/detail.html', {'foods': foods})
