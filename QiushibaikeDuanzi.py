# -*- coding: utf-8 -*-
__author__ = 'Yu'

import urllib.request,time,chardet,os
from bs4 import BeautifulSoup

import urllib.request,time,chardet,os
from bs4 import BeautifulSoup

class qbdzDownloader(object):
    def __init__(self,fileDir=r'D:\SpyderDownload\content.txt'):
        self.fileDir=fileDir


    def getReq(self,url):
        headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'}
        req=urllib.request.Request(url,headers=headers)
        return req


    def DownloadImage(self,imageUrl,imageDir):
        if os.path.exists(imageDir):
            return False
        req=self.getReq(imageUrl)
        image=urllib.request.urlopen(req).read()
        with open(imageDir,'wb') as fhand:
            fhand.write(image)
        return True

    def downloadContent(self,PageUrl):
        req=self.getReq(PageUrl)
        rawHtml=urllib.request.urlopen(req).read()
        encoding=chardet.detect(rawHtml)['encoding']
        html=rawHtml.decode(encoding=encoding)
        soup=BeautifulSoup(html,'lxml')
        tags=soup.findAll('div',{'class':'article block untagged mb15'})
        with open(self.fileDir,'w+') as fhand:
            for tag in tags:
                time.sleep(2)
                text=tag.findAll('div',{'class':'content'})[0].text
                fhand.write(text)


qbd=qbdzDownloader()
PageUrl=r'http://www.qiushibaike.com/'
qbd.downloadContent(PageUrl)