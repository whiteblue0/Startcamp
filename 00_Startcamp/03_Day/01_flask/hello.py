from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'


#terminal 입력: FLASK_APP=hello.py flask run
# 서버에 응답 요청>>서버가 할당된 주소값에 요청 응답