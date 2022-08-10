import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://rank-king.jp/article/13241'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', class_='p-ranking-product__top')
    for item in items:
        maker_and_flour = item.text
        print(maker_and_flour)


if __name__ == '__main__':
    main()
