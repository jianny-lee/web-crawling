import requests
from bs4 import BeautifulSoup

url = 'https://codeup.kr/problemsetsol.php?psid=33'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    i = 1
    title_list = []
    for i in range(98):
        # html에서 문제명들 selector 경로를 이용하여 가져와서 list에 넣어줌
        title = soup.select_one('#problemset > tbody > tr:nth-child('+ str(i+1) + ') > td:nth-child(3) > div > a''')
        title_list.append(title.get_text())

else :
    print(response.status_code)

print(title_list)

# 새로운 텍스트 파일에 입력
j = 6001
with open('./resource/title-lists.txt','w') as f:
    for i in title_list:
        f.write('| ')
        f.write(str(j)) #번호명
        f.write(' | ')
        f.write(i) #문제명
        f.write(' |')
        # f.write(' |\n') #문제 풀이일, 이건 하나씩 채워갈 예정
        if(j<=6025):
            f.write(' 2021.07.13 |\n')
        else:
            f.write(' |\n')
        j+=1
