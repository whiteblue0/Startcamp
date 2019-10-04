# Django_tutorial(crud)

crud란? create, read, update, delete

개발환경 - vscode

1. 환경 구축하기

   - 가상환경 설정: cmd - ```source venv/Scripts/activate```

     - django 설치: cmd - ```pip install django```

   - 프로젝트 생성: cmd - ```django-admin startproject projectname .```    (※ projectname = 프로젝트명)

     - 앱 기본환경 구축: ```python manage.py startapp appname``` (※ appname == 앱 이름)

       -- settings.py 설정

       INSTALLED_APPS list에 'appname' 요소 추가

       project 폴더에 templates 폴더, base.html 생성

       경로 설정: TEMPLATES >> 'DIRS'값:```[os.path.join(BASE_DIR, 'projectname', 'templates')]```

       LANGUAGE_CODE = 'ko-kr'

       TIME_ZONE = 'Asia/Seoul'

       -- base.html 설정(위치:root/projectname/templates/base.html)

       html 기본페이지 생성 >> ! tab

       bootstarp 추가

       --appname 폴더에 templates 폴더, templates/appname 폴더 생성

       

       --urls.py 설정

       django.urls 모듈에서 path 모듈과 함께 include 모듈 추가

       app url path 추가```path('appname/', include('appname.urls'))```

       /* 이 작업으로  app url 분산관리 가능*/

       -- manage.py 설정

       [migration]

       step1. cmd >> python manage.py makemigrations

       step2. cmd >> python manage.py migrate

       
       
       [admin]
       
       admin 생성: cmd >> python manage.py create superuser ( migration 선행필수)

2. 내용 구성

   - models.py >> 사용할 class 생성

     class 생성시 class변수=models.Model

   - base.html extend: body section

      body 태그 내부에

     `<div class="container">`

     {% block body %}{% endblock %} 입력 - {% extends 'base.html' %} 로 html 확장 사용

     `</div>`

   - view.py : html페이지를 불러올 함수 설정

     - ```from .models import Article``` == models.py의 class 로드

     crud에서 사용할 함수 list: 

     ```index(request), new(request),create(request),delete(request,pk),edit(request,pk),update(request)```
   
     
   
   - index(==Main) 생성
   
     - index.html 경로: root/appname/templates/articles/index.html
   - url.py에서 path 설정: ```path('주소', views.index)
     
   - def new:
   
     - appname/new.html 렌더링
     - new.html 생성 - form tag 작성으로 class 요소 입력