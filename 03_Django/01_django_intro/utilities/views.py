from django.shortcuts import render
from decouple import config
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

def mamago(request):
    return render(request, 'utilities/mamago.html')

def translated(request):
    word = request.GET.get('word')

    #네이버에 번역 요청을 보낼 준비(.env에서 ID, SECRET 값 불러오기)
    naver_client_id=config('NAVER_CLIENT_ID')
    naver_client_secret=config('NAVER_CLIENT_SECRET')

    #요청 보낼 url
    mamago_url = 'https://openapi.naver.com/v1/papago/n2mt'

    # header 정보 구성
    headers = {
        'X-Naver-Client-Id':naver_client_id,
        'X-Naver-Client-Secret':naver_client_secret
    }

    #5. 요청 데이터 준비
    data = {
        'source': 'ko',
        'target': 'en',
        'text': word
    }

    #6. 네이버 요청을 보내자!
    mamago_response = requests.post(mamago_url, headers=headers, data=data).json()
    # print(mamago_response)

    #7. 번역된 텍스트 추출
    result = mamago_response.get('message').get('result').get('translatedText')

    context = {
        'kor': word,
        'eng':result
    }

    return render(request, 'utilities/translated.html', context)