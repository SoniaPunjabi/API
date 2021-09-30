from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

def Stackoverflow(request):
    question = {}
    if 'question' in request.GET:
        username = request.GET['question']
        url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
        response = requests.get(url)
        question = response.json()
        for data in response.json()['items']:
            print(data['title'])


    return render(request, 'polls/stackoverflow.html', {'question': question})