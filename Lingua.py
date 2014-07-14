__author__ = 'fish'
import urllib2
import requests

word = 'help'
mail = ''
passwd = ''

link = 'http://api.lingualeo.com/gettranslates?word=' + word

cookie = {'servid':'f3a14c0aa1828146590a5c0e5bcefe1a7741d68d51c12d25e6ba40da7918893ed2d7963628da7252',
          "userid":"3299",
          "AWSELB" :"75C701150A9420ACA77B49A59BB2636792D3E5911E677A65153DA70A80FDAAD4FB2493A73BAFD8779ADEAAAC382AFA7952EDE5B45F6C8A9C148E59341A1745F2BD0BEABDA2917467E67EE73E125B9EDCB7159DE56D",
          "remember":"e30c0000af17f67875ab20ad59d1ed6aa5c8161a4876d31e25ee67f1996883d45e06b1058abdfa0d"}

hit = requests.get(url=link, cookies=cookie)
translation = ((hit.text).split(',')[7]).split(":")[1]
picture = ((((hit.text).encode('ascii', 'replace')).split(',')[5]).split('"')[3]).replace('\\', '')
sound = ((((hit.text).encode('ascii', 'replace')).split(',')[-1]).split('"')[3]).replace('\\', '')

def save_file():
    with open('/Users/fish/' + word + '.jpg', 'wb') as handle:
        response = requests.get(picture, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

    r = requests.get(picture)
    with open("picture.jpg", "wb") as code:
    code.write(r.content)

def get_sound(word):
    url = "http://translate.google.com/translate_tts?tl=en&q=" + word
    request = urllib2.Request(url)
    request.add_header('User-agent', 'Mozilla/5.0')
    opener = urllib2.build_opener()

    f = open(word + ".mp3", "wb")
    f.write(opener.open(request).read())
    f.close()
    print "OK"
    return 0

def create_cookie(cookie):
    test = cookie.cookies.extract_cookies.im_self.get('servid')
    print test

def login(email, password):
    url = 'http://lingualeo.ru/ru/login'
    data = {'email': email, 'password': password}
    r = requests.post(url=url, data=data)
    cookie = create_cookie(r.cookies)
    return cookie

def main():

# cookie = login(mail, passwd)
#print cookie
    #print create_cookie(cookie)
    #cookie = {'servid':'f3a14c0aa1828146590a5c0e5bcefe1a7741d68d51c12d25e6ba40da7918893ed2d7963628da7252',"userid" : "3299", "AWSELB" : "75C701150A9420ACA77B49A59BB2636792D3E5911E677A65153DA70A80FDAAD4FB2493A73BAFD8779ADEAAAC382AFA7952EDE5B45F6C8A9C148E59341A1745F2BD0BEABDA2917467E67EE73E125B9EDCB7159DE56D","remember" : "e30c0000af17f67875ab20ad59d1ed6aa5c8161a4876d31e25ee67f1996883d45e06b1058abdfa0d"}
    #print requests.get(url='http://api.lingualeo.com/gettranslates?word=help',cookies=cookie).text


if __name__ == '__main__':
    main()


