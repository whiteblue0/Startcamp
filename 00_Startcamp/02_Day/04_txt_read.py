#1. 파일 읽기(예전방식)

# f = open('ssafy.txt','r')
# all_text = f.read()
# print(all_text)
# f.close()


#2-1. 파일 읽기(최신 방식)
# with open('with_ssafy.txt', 'r') as f:
#     all_text = f.read()
#     print(all_text)




# #1-2. 파일 읽기(예전 방식2) -readlines()
# f = open('ssafy.txt','r')
# lines = f.readlines()
# print(lines)

# for line in lines:
#     print(line)

# f.close()


#2-2. 파일 읽기(최신) 방식2) -readlines()
with open('with_ssafy.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())