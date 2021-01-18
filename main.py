import requests
from bs4 import BeautifulSoup

# respon = requests.Session()
def login():
    print('test login')
    urls = "https://www.yelp.com/search?cflt=contractors&find_loc=St%20Francis%20Wood%2C%20San%20Francisco%2C%20CA&start"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

    respon = requests.get(urls, headers=headers)
    f = open('./re.html', 'w+')
    f.write(respon.text)
    f.close()

    soup = BeautifulSoup(respon.text, 'html5lib')

    page_item = soup.find_all('div', attrs={'class': 'pagination-link-container__09f24__13AN7'})
    # total_page = len(page_item)

    paginition = '1 of 12'
    total_page = paginition.split('of')[1]
    total_page = int(total_page)
    print(total_page)


    print(len(page_item))

    return total_page

def get_url(page):
    print('test url ... page {}'.format(page))
    params = {
        'start': page
    }

    respon = requests.get('https://www.yelp.com/search?cflt=contractors&find_loc=St%20Francis%20Wood%2C%20San%20Francisco%2C%20CA&start', params=params)
    

    suop = BeautifulSoup(respon.text, 'html5lib')
    # suop = BeautifulSoup(open('./re.html'), 'html5lib')

    titles = suop.find_all('span', attrs={'class': 'text__09f24__2tZKC text-color--black-regular__09f24__1QxyO text-align--left__09f24__3Drs0 text-weight--bold__09f24__WGVdT text-size--inherit__09f24__2rwpp'})

    urls = []
    for title in titles:
        url = title.find('a')['href']
        # urls.append(url)
        print(url)
        # print(url)
    # print(urls)
    # print(suop)

    return  urls

    # f = open('./re.html', 'w+')
    # f.write(respon.text)
    # f.close()


def get_detail():
    print('test ...')
    # pass


def create_csv():
    pass


def run():
    total_page = login()

    total_urls = []
    for i in range(total_page):
        page = i + 1

        # print(page)
        urls =  get_url(page)
        total_urls += urls
    
    print(total_urls)
    print(len(total_urls))


if __name__ == '__main__':
    run()
