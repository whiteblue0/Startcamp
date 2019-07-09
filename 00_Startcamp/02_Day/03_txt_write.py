#1. 옛날방식
# f = open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line{i}.\n')
# f.close()

#2. 파일 쓰기(최신)

with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line{i}.\n')