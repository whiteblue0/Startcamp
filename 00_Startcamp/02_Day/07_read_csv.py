#csv 파일 read 방법 2가지

#1. split
# with open('lunch.csv','r',encoding= 'utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())
#         print(line.strip().split(','))


#csv reader

import csv

with open('lunch.csv', 'r',encoding= 'utf-8') as f:
    lines = csv.reader(f)
    
    for line in lines:
        print(line)
