from django.shortcuts import render
from datetime import datetime
import random, requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

#2. Template Variable(탬플릿 변수)
def dinner(request):
    menu = ['족발','햄버거','치킨','초밥']
    pick = random.choice(menu)
    context = {'pick':pick}
    return render(request, 'dinner.html', context)

def images(request):
    return render(request, 'images.html')

#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    names = ['justin','john','jason','juan', 'zzulu']
    name  = random.choice(names)
    menu = ['족발','햄버거','치킨','초밥']
    pick = random.choice(menu)
    context = {'name':name,
    'age':age,
    'pick':pick
    }
    return render(request, 'hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
#4-2. 2개의 숫자를 인자로 받아(num1, num2) 곱셉 결과를 출력

def introduce_2(request, name, age):
    context = {'name':name,
    'age':age
    }
    return render(request, 'introduce_2.html', context)

def mult(request, num1, num2):
    result = num1 * num2
    context = {
        'num1':num1,
        'num2':num2,
        'result':result
    }
    return render(request, 'mult.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오.
def Circle(request, r):
    area = 3.14 * r
    context = {
        'area':area,
        'r':r
    }
    return render(request, 'Circle.html', context)

#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucmber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages':messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list
    }
    return render(request, 'template_language.html', context)

#13workshop
def info(request):
    teacher = 'Justin'
    students = ['홍길동','김길동','박길동']
    context = {
        'teacher': teacher,
        'students': students
    }
    return render(request, 'info.html', context)

def student(request):
    students = ['홍길동', '김길동', '박길동']
    context = {
        'students': students,
    }
    return render(request, 'student.html', context)


#6. 실습
#6-1. isbirth
#today.month -> 8 / today.day -> 6
# True/Flase를 담아 isbirth.html로 넘겨 DTL(템플릿 문법-조건문) 활용

def isbirth(request):
    today = datetime.now()
    if  today.month == 8 and today.day == 6 :
        result = True
    else:
        result = False
    context = {
            'result':result
        }

    return render(request, 'isbirth.html', context)

#6-2. 회문판별(palindrome)
def ispal(request, word):
    result = False
    if word == word[::-1]:
        result = True

    context= {
        'word':word,
        'result':result
    }
    return render(request, 'ispal.html', context)

#6-3. 로또 번호 추첨
#lottos -> 1 ~ 45까지의 번호 중 6개를 랜덤으로 pick한 리스트
#real_lottos -> [21, 24, 30, 32, 40, 42]
# lottos 번호를 하나씩 출력(DTL-for문)
# 컴퓨터가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기

def lottos(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = list(random.sample(range(1,26), 6))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }

    return render(request, 'lottos.html', context)


#7. Form - GET

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message':message,
        'message2':message2,
    }
    return render(request, 'catch.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    pong = request.GET.get('ping')
    context ={
        'pong':pong
    }

    return render(request, 'pong.html', context)


#7 Form - GET 실습(ascii artii)
def art(request):
    return render(request, 'art.html')

def result(request):
    word = request.GET.get('word')
    fonts= requests.get('http://artii.herokuapp.com/fonts_list').text
    fonts = fonts.split('\n')
    
    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서
    # font라는 변수에 저장(str)
    font = random.choice(fonts)

    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result':result,
    }

    return render(request, 'result.html', context)

#9. Form - POST
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name':name,
        'password':pwd
    }

    return render(request, 'user_create.html', context)
