# -*- coding: utf-8 -*-
import re

import requests
import random
from bs4 import BeautifulSoup

def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/text/').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class':'content'}):
        print div.text.strip()
        print '\n'

def demo_string():
    stra = 'hello world'
    print stra.capitalize();
    print stra.replace('hello', 'hi')

    strb = '\r\naaabbbccc\r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    print 3, len(stra), len(strb)
    print 4, '-'.join(['a', 'b', 'c'])
    print 5, stra.split(' ')

def demo_operation():
    for i in range(0, 10):
        if i == 0:
            pass
        if i == 3:
            continue
        if i < 5:
            print i
        if i == 7:
            break

def demo_list():
    lista = [1,2,3]
    print 1, lista
    listb = ['a', 1, 1.1]
    print 2, listb
    listc = [1,2,3,4,5]
    for i in listc:
        print i

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def demo_dict():
    dicta = {4 : 16, 1 : 1, 2 : 4, 3 : 9, 'a' : 'alone'}
    # print dicta
    for key,value in dicta.items():
        print key, value

    print 9999, dicta.has_key(4), dicta.has_key('i')
    dictxx = {'+' : add, '-' : sub}
    print 6, dictxx['+'](1,2)


def demo_set():
    lista = (1,2,3)
    seta = set(lista)
    print  1, seta

class User:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im' + self.name + '' + str(self.uid)

class Guest(User):
    def __repr__(self):
        return 'im guest ' + self.name

def demo_obj():
    user1 = User('jim', 1)
    print user1
    guest1 = Guest('lily', 2)
    print guest1

def demo_random():
    # random.seed(1)
    for i in range(0,5):
        print  random.randint(0,100)
    print int(random.random() * 100)

def demo_regex():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    print 1,p1.findall(str)
    p2 = re.compile('[\d]')
    print 2, p2.findall(str)

    emailstr = 'aaaa@163.com,bbbb@qq.com,ccc@gmail.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 'email:', p3.findall(emailstr)

    str = 'xx2018-01-11zzz'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print p5.findall(str)

    str = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 'web', p4.findall(str)

if __name__ == '__main__':
    # demo_random()
    demo_regex()
    # demo_obj()
    # demo_set()
    # demo_dict()
    # demo_list()
    # demo_operation()
    # demo_string();
    # qiushibaike()
    # print 'hello world!'