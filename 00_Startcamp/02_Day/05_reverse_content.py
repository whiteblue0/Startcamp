# #역순으로 출력 방법1
# with open('with_ssafy.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip()[::-1])

#역순 출력 방법2
with open('writelines_ssafy.txt','r') as f:
    lines = f.readlines()

lines.reverse()

with open('reverse_ssafy.txt','w') as f:
    for line in lines:
        f.write(line)