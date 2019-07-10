#cdv파일 사용법

lunch = {
    '선산곱창':'054-123-4968',
    '땅땅치킨':'054-584-1738',
    '평양면옥':'054-986-8834'
}

#1. 방법1
with open('lunch.csv','w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')