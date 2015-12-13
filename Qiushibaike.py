# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:28:20 2015

@author: Yu
"""
import urllib.request,time,chardet,os
from bs4 import BeautifulSoup

class qbDownloader(object):
    def __init__(self,path):
        self.path=path


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

    def downloadImages(self,PageUrl):
        req=self.getReq(PageUrl)
        rawHtml=urllib.request.urlopen(req).read()
        encoding=chardet.detect(rawHtml)['encoding']
        html=rawHtml.decode(encoding=encoding)
        soup=BeautifulSoup(html,'lxml')
        nodes=soup.findAll('div',{'class':'mala-text'})
        for node in nodes:
            time.sleep(2)
            imageUrl=node.img.attrs['src']
            imageName=node.img.attrs['alt']+imageUrl[-4:]
            imageDir=self.path+'\\'+imageName
            if not self.DownloadImage(imageUrl,imageDir):
                print('%s has already existed'%imageName)
                continue






path=r'D:\SpyderDownload\Qiubaichengren'
qbd=qbDownloader(path)
for i in range(1,2):
    url='http://www.qiubaichengnian.com/index_%d.html'%i
    qbd.downloadImages(url)