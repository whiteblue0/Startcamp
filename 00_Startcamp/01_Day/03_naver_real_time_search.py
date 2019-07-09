import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')
realtime = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div ")
# print(type(realtime))

# for item in realtime:
#     print(item.text)

for idx, item in enumerate(realtime):
    print(f"{idx+1}위: {item.text}")