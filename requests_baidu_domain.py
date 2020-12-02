#!/usr/local/python/bin/python3.7
# -*- coding: UTF-8 -*-
import requests,re,time,random,string
#error='360搜索_访问异常出错' 			 		 #360
error="location.href.replace"  #baidu
url=["baidu.com"]
uaList = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36']
with open('a.txt','r') as f:
     c=list(f.readlines()) 
for i in c: 
     ci=(i.rstrip("\n"))
     u='https://www.baidu.com/s?wd={}'.format(ci) 		#baidu
     #u='https://so.com/s?q={}&pn=1'.format(ci)      		 #360
     sj=random.randrange(10,15)
     #time.sleep(sj)
     header={'User-Agent': random.choice(uaList)}
     a=requests.get(u,headers=header).content.decode('utf-8')
     if error in a:
         print(ci,"error")
         continue
     lb=re.findall(r"\"text-decoration\:none\;position\:relative\;\"\>(.*)?\/", a)     #baidu
     #lb=re.findall(r"\<cite\>(.*?)</cite\>",a) 			     #360
     strlb=''.join(lb)
     z="不在"
     for i in  url:
         if i in strlb:
            z="在"
            break
     print(ci,z)
