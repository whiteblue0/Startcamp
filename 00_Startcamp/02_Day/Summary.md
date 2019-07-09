
``` import os
import random

for i in range(500):
    cmd = f"touch ./dummy/{i+1}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd) ```

os.system으로 dummy 생성


``` import os

os.chdir(r'C:\Users\student\TIL\00_Startcamp\02_Day\dummy')

for filename in os.listdir('.'):
    os.rename(filename, filename.rename('SAMSUNG_','SSAFY')) ```

file.rename으로 파일명 변경하는 함수

``` .wirte()```
txt에 입력하는 함수