# -*- coding: utf-8 -*-
from pyquery import PyQuery
import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
    q = PyQuery(open('v2ex.html').read())
    print q
    # print q('title').html()
    # print q('title').text()
    #
    # for each in q('div.inner>a').items():
    #     if each.attr.href.find('tab') > 0:
    #         print 1,each.attr.href
    #
    # for each in q('#Tabs>a').items():
    #     print 2, each.attr.href
    #
    #
    # for each in q('span.item_title>a').items():
    #     print 3, each.html()
    #
    # for each in q('.cell>a[href^="/go/"]').items():
    #     print 4, each.attr.href
    #
    # for each in q('.cell a[href^="/go/"]').items():
    #     print 5, each.attr.href

    for each in q('span.item_title>a').items():
        print 6, each.html()