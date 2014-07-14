__author__ = 'fish'
# -*- coding: utf-8 -*-
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf8")
mail = '2543810@gmail.com'
passwd = 'aC1IHR'
r = ''
cookie = {}
w = ''
words = (
'absence', 'account', 'actuality', 'adjustment', 'administer', 'adversary', 'advertisement', 'agreement', 'amusement',
'apparatus')


def download_file():
    with open('/Users/fish/' + word + '.jpg', 'wb') as handle:
        response = requests.get(picture, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)


def make_word(so):
    global w
    word = ((so).split(',')[3]).split('"')[3]
    transcription = (((so).split(',')[-4]).split(':')[1]).encode('utf-8')
    translation = ((so).split(',')[7]).split(":")[1]
    picture = ((((so).encode('ascii', 'replace')).split(',')[5]).split('"')[3]).replace('\\', '')
    sound = ((((so).encode('ascii', 'replace')).split(',')[-1]).split('"')[3]).replace('\\', '')
    return save_files(w, (transcription).split('"')[1], (translation).split('"')[1], (picture).split('/')[-1],
                      (sound).split('/')[-1])


def save_files(word, transcription, translation, picture, sound):
    with open('test1.txt', 'a') as handle:
        handle.write(
            '\n' + word + '\t' + transcription + '\t' + translation + '\t' + '<img src="' + picture + '">' + '\t' + '[sound:' + sound + ']')

def login(email, password):
    global r
    global cookie
    url = 'http://lingualeo.ru/ru/login'
    data = {'email': email, 'password': password}
    r = requests.post(url=url, data=data)
    cookie = {'servid': (r.cookies.extract_cookies.im_self.get('servid')),
              "userid": "3299",
              "AWSELB": (r.cookies.extract_cookies.im_self.get('AWSELB')),
              "remember": "e30c0000af17f67875ab20ad59d1ed6aa5c8161a4876d31e25ee67f1996883d45e06b1058abdfa0d"}
    return


def ask_leo(word):
    """

    Делаем запрос в ЛингваЛео по заданому слову и возвращаем его значение в функцию make_word
    """
    global w
    link = 'http://api.lingualeo.com/gettranslates?word=' + word
    hit = requests.get(url=link, cookies=cookie)
    w = word
    return make_word(hit.text)

def main():
    login(mail, passwd)
    for word in words:
        ask_leo(word)

if __name__ == '__main__':
    main()