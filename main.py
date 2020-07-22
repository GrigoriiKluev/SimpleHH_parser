import requests
from bs4 import BeautifulSoup as bs


headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

           }
base_url = 'https://voronezh.hh.ru/search/vacancy?text=Python+&only_with_salary=false&clusters=true&enable_snippets=true'

def hh_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers= headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.findAll('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title= div.find('a', attrs= {'data-qa': 'vacancy-serp__vacancy-title'}).text
            href= div.find('a', attrs= {'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs= {'data-qa':'vacancy-serp__vacancy-employer'}).text
            print(href +'\n' + title +'\n' + company  )
    else:
        print('ERROR')

hh_parse(base_url, headers)