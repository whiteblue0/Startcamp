#1. pyformat

# name = '홍길동'
# english_name = 'hong'

# print('안녕하세요, {}입니다. my name is {}'.format(name,english_name))



#2. f-strings

# name = '홍길동'
# print(f'안녕하ㅔ요,{name}입니다.')


# menu = ['파스타','김밥','홍콩반점']
# import random
# lunch = random.choice(menu)


import random

numbers = list(range(1,46))
lotto = random.sample(numbers,6)
print(f'오늘의 로또 번호는 {sorted(lotto)}')


