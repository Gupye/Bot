import requests
import bs4
def get_proxies():
    html = requests.get('https://mtproto-proxy.fun')
    code = html.text
    soup = bs4.BeautifulSoup(code, 'lxml')
    list = []
    raw_text = soup.find_all('tr')
    a = len(raw_text)
    for i in range(1, a - 1):
        text = str(raw_text[i].find('a'))
        text = text.split('=')

        server = text[2].split(';')[0].split('&')[0]
        port = text[3].split('&')[0]
        secret = text[4].split('"')[0]
        data = {'server': server,
                'port': port,
                'secret': secret}
        list.append(data)
    # ser = list[0]['server']
    # port = list[0]['port']
    # PROXY = str(f'socks5://{ser}:{port}')
    # print (PROXY)
    return list
    # print(list[2]['server'])

if __name__ == '__main__':
    get_proxies()