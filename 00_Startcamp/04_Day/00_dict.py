lunch = {
    '중국집':'02',
    }

lunch = dict(중국집='02')
# print(lunch)

lunch['분식집'] = '031'

idol = {
    'bts':{
        '지민':24,
        'RM': 25
    }
}



#3. 딕셔너리 value 가져오기
#print(idol['bts']["RM"])
#print(idol.get('bts').get('RM'))

# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2.  .items() -  key, value 모두 가져오기
# for key, value in lunch.items():
#     print(key,value)

#4-3.  .values() -  value만 가져오기
# for value in lunch.values():
#     print(value)


#4-4.  .keys()  -  key만 가져오기
for key in lunch.keys():
    print(key)