from django.shortcuts import render
from .models import Job
from faker import Faker
from decouple import config
import requests

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')
    person = Job.objects.filter(name=name).first()

    if person:
        past_job = person.past_job
    else:
        fake = Faker('ko_KR')
        past_job = fake.job()
        person = Job(name=name, past_job=past_job)
        person.save()
    
    #GIPHY
    #api key 가져오기
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    # 요청 url 세팅
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=8&lang=ko'
    #요청 보내기
    data = requests.get(url).json()
    # image 추출
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None

    context = {'person': person}
    return render(request, 'jobs/past_life.html', context)