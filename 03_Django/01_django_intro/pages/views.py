from django.shortcuts import render
from datetime import datetime
import random

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
    ages = [28, 27 ,24]
    
    context = {
        'students': students,
        'ages': ages
    }
    return render(request, 'student.html', context)
