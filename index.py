#!E:\python2.7\python.exe
# -*- coding: UTF-8 -*-

#print "Content-type:text/html;charset=utf-8"
print

import urllib2
import urllib
import re
from db import *
db=WebSiteDB()
class Dbbd:

    def __init__(self):
        self.url = "http://news.baidu.com/"
    
      # convert div to ''
    def tranTags(self, x):
        pattern = re.compile('<div.*?</div>')
        res = re.sub(pattern, '', x)
        return res

    def getUrl(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getNavCode(self):
        page= self.getUrl()
        #print page 
        pattern = re.compile('(<div id="menu".*?)<i class="slogan"></i>', re.S)
        navCode = re.search(pattern,page)
        return navCode.group(1)
        
    #get nav
    def getNav(self):
        navCode = self.getNavCode()
        pattern = re.compile('<a href="(http://.*?/).*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern, navCode)
        # return itmes
        for item in itmes:
            sql = "INSERT INTO news (n_url,n_name) values ('%s','%s')" %(item[0],self.tranTags(item[1]))
            db.insertOneRd(sql)
            # print  item[0], self.tranTags(item[1])
    
    def getTitl(self):
        getUrl= self.getUrl()
        pattern = re.compile('(<div id="pane-news".*?)<div class=".*?" id="tupianxinwen">', re.S)
        code = re.search(pattern,getUrl)
        return  code.group()

    def getTitle(self):
        getTitl = self.getTitl()
        pattern = re.compile('<a href="(http://.*?").*?>(.*?)</a>', re.S)
        items = re.findall(pattern,getTitl)
        return items
    def toimg(self,data):
        res=re.compile('<img.*?>')
        content = re.sub(res,'',data)
        return content


news = Dbbd()
items=news.getTitle()   
for item in items:
    sql = "INSERT INTO news (n_url,n_name) values ('%s','%s')" %(item[0],news.toimg(item[1]))
    ac=db.insertOneRd(sql) 
    