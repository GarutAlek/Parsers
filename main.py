from bs4 import BeautifulSoup as BS
import requests
import random
import os


def parseImg(url):
    headers = {'User-agent': 'Mozilla/5.0'}
    html = requests.get(url, headers=headers).text
    soup = BS(html, 'lxml')
    quotes_img = soup.find_all('img', class_='no-click screenshot-image')
    for i in quotes_img:
        tmp = i.get('src')
        if tmp[-21:] != '0_173a7b_211be8ff.png':
            return tmp


def base_create():
    with open('url_base.txt', 'w') as writer:
        for i in range(5000):
            i1 = random.randrange(0, len(alp) - 1)
            i2 = random.randrange(0, len(alp) - 1)
            i3 = random.randrange(0, len(alp) - 1)
            i4 = random.randrange(0, len(alp) - 1)
            i5 = random.randrange(0, len(alp) - 1)
            url = 'https://prnt.sc/' + alp[i1] + alp[i2] + alp[i3] + alp[i4] + alp[i5]
            url_baseList.append(url)
            writer.write(url + '\n')


if __name__ == '__main__':
    alp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # put your dir, where you want to get a base of working urls and images
    os.chdir(r"CHANGEDIR")
    url_baseList = []

    # with open('url_base.txt','r') as file:
    #     for i in range(500):
    #         url_baseList.append(file.readline())
    #
    # for i in range(500):
    #     url_baseList[i] = url_baseList[i][:-1]

    # use it 1 time, then use code above
    base_create()

    # creating a base of working urls
    # it takes a significant amount of time
    with open('working_url_base.txt', 'w') as file:
        for url in url_baseList:
            https = parseImg(url)
            if https is not None:
                file.write(https + '\n')

    # if you want to download images then use code below
    working_url_baseList = []
    with open('working_url_base.txt', 'r') as file:
        for i in range(5000):
            working_url_baseList.append(file.readline())

    for i in range(5000):
        working_url_baseList[i] = working_url_baseList[i][:-1]

    for https in working_url_baseList:
        img_data = requests.get(https).content
        with open(https[-9:], 'wb') as handler:
            handler.write(img_data)
