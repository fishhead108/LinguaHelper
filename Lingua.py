__author__ = 'fish'
# -*- coding: utf-8 -*-
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf8")

# Variables
class Variables():
    def __init__(self):
        self.mail = raw_input('Введите ваш email:\n')
        self.passwd = raw_input('Введите ваш пароль:\n')
        self.filename = raw_input('Введите название файла для выгрузки в Anki:\n')
        self.r = ''
        self.cookie = {}
        self.w = ''
        self.words = ()


def create_wordslist():
    """
    Open file with words and read them into list.
    """
    global words
    with open('C:\\Users\\Dmitriy\\Documents\\Anki\\fish\\test.txt') as f:
        words = (f.read()).split('\n')
    return


def login(email, password):
    """
    Login to LinguaLeo.
    """
    global r
    global cookie
    url = 'http://lingualeo.ru/ru/login'
    data = {'email': email, 'password': password}
    r = requests.post(url=url, data=data)
    cookie = {'servid': (r.cookies.extract_cookies.im_self.get('servid')),
              "userid": "3299",
              "AWSELB": (r.cookies.extract_cookies.im_self.get('AWSELB')),
              "remember": "e30c0000af17f67875ab20ad59d1ed6aa5c8161a4876d31e25ee67f1996883d45e06b1058abdfa0d"}


def ask_leo(word):
    """
    Do the query to LinguaLeo with chosen word and return value to function make_word.
    """
    global w
    link = 'http://api.lingualeo.com/gettranslates?word=' + word
    hit = requests.get(url=link, cookies=cookie)
    w = word
    return make_word(hit.text)


def make_word(so):
    """
    Getting definitions of the word.
    """
    global w
    # word = ((so).split(',')[3]).split('"')[3]
    transcription = (((so).split(',')[-4]).split(':')[1]).encode('utf-8')
    translation = ((so).split(',')[7]).split(":")[1]
    picture = ((((so).encode('ascii', 'replace')).split(',')[5]).split('"')[3]).replace('\\', '')
    sound = ((((so).encode('ascii', 'replace')).split(',')[-1]).split('"')[3]).replace('\\', '')
    download_file(sound)
    download_file(picture)
    return save_files(w, transcription.split('"')[1], translation.split('"')[1], picture.split('/')[-1],
                      sound.split('/')[-1])


def download_file(file):
    """
    Downloading image and audio files.
    """
    r = requests.get(file)
    with open('C:\\Users\\Dmitriy\\Documents\\Anki\\fish\\collection.media\\' + file.split('/')[-1], "wb") as code:
        code.write(r.content)


def save_files(word, transcription, translation, picture, sound):
    """
    Saving values into file for next import to Anki.
    """
    with open('C:\\Users\\Dmitriy\\Documents\\Anki\\fish\\' + filename + '.txt', 'a') as handle:
        handle.write(
            '\n' + word + '\t' + transcription + '\t' + translation + '\t' + '<img src="' + picture + '">' + '\t' + '[sound:' + sound + ']')


def instruction():
    """
    Writes instruction after installation.
    """
    print ('Чтобы произвести импорт карточек в Anki:\n'
           '1) Запустите Anki.\n'
           '2) В меню выберите Файл-Импортировать.\n'
           '3) В меню выберите файл который вы сохранили вначале.')


def main():
    """
    Main entry point for the script.
    """
    login(mail, passwd)
    create_wordslist()
    for word in words:
        print word
        ask_leo(word)
    instruction()


if __name__ == '__main__':
    sys.exit(main())