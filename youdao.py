#!/usr/bin/python
# -*- coding: utf8 -*-
from pyquery import PyQuery as pyq
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def translate():
    url = r'http://dict.youdao.com/search?q=' + sys.argv[1]
    doc = pyq(url)
    doc('#custheme').remove()
    doc('.c-topbar').remove()
    doc('.c-subtopbar').remove()
    doc('.c-header').remove()
    doc('#c_footer').remove()
    doc('.c-bsearch').remove()
    doc('#ads').remove()
    doc('#rel-search').remove()
    doc('.error-wrapper').remove()
    doc('#topImgAd').remove()
    doc('#container').css('margin', '0')
    doc('#results-contents').css('width', '510px')
    doc('#results-contents').css('margin', '0')
    doc('#result_navigator').css('left', '550px')
    for a in doc('a'):
        href = a.get('href')
        if href is not None and href.startswith('/'):
            a.make_links_absolute('http://dict.youdao.com')

    link = u"<a href='" + url + u"'>在浏览器中查看翻译</a>"
    doc('#results-contents').append(link)
    print doc.outerHtml()


if __name__ == "__main__":
    translate()
    sys.exit(0)
