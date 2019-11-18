1. remote 작업 로직 

   편의상 A(SSAFY), B(집) 이라고 할게요!

   - A에 최초 `config` 등록

     ```bash
     # 최초 1회만 설정하면 됨
     
     # git cofig 등록
     $ git config --global user.name "이름"
     $ git config --global user.email "github 등록 이메일"
     
     # 등록 확인
     $ git config --global --list
     ```

   - A에서 작업 후 `add` -> `commit` -> `push(github에 push)`

   - B에서 최초 `git clone [A에서 push한 remote repo HTTPS 주소]`

   - B에 `config` 등록 -> A에서 등록한 내용과 동일하게 작업

     ```sh
     # 최초 1회만 설정하면 됨
     
     # git cofig 등록
     $ git config --global user.name "이름"
     $ git config --global user.email "github 등록 이메일"
     
     # 등록 확인
     $ git config --global --list
     ```

   - B에서 작업을 마무리 하고 `add` -> `commit` -> `push`

   - A에서 clone 실시 -> 작업 이후는 위와 동일
   - B에서 Clone 실시 -> 작업 이후는 위와 동일

2. 계정 정보가 바뀐 경우 대응

   ```sh
   #1. credential 제거
   $ git credential reject
   protocol=https
   host=lab.ssafy.com # 혹은 github.com
   
   #2. 새로 클론 받기 -> 로그인 정보를 물어보면 그대로 입력
   #3. 새로 작업 수행
   #4. add -> commit
   $ git add .
   $ git commit -m "커밋 메시지"
   
   #5. remote 이름(별명) 변경(option)
   # clone을 받으면 기본적으로 설정되는 remote name은 origin
   $ git remote rename [기존 이름] [변경 할 이름]
   
   #6. remote 저장소에 push
   $ git push [리모트 저장소 별명] master
   
   # 참고 - 리모트 저장소 별명 삭제
   $ git remote rm [삭제하고자 하는 저장소 이름]
   ```

   