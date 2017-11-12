#author:zhousc
import requests,re
import json

class HtmlParser(object):

    def html_parser(self, url,payload):
        # 商品网页解析
        if url==None:
            return
        html=requests.get(url,params=payload)
        if html.status_code ==200:
            html.encoding='uft-8'
            print("正在解析网址:%s"%html.url )
            regex = 'g_page_config = (.+)'
            items = re.compile(regex).findall(html.text)
            items = items.pop().strip()
            items = items[0:-1]
            items = json.loads(items)
            return items

    def tag_parser(self,url,payload):
        if url==None:
            return
        html=requests.get(url,params=payload)
        if html.status_code==200:
            #html.encoding='utf-8'
            print("正在解析产品标签:%s"%html.url)
            regex= '"tagClouds":(.*)}'
            items = re.compile(regex).findall(html.text)
            items = items.pop()
            items = json.loads(items)
            return items

    def rate_parser(self,url,payload):
        if url==None:
            return
        html=requests.get(url,params=payload)
        if html.status_code == 200:
           # html.encoding='utf-8'
            print("正在解析评论网页：%s"%html.url)
            regex = '"rateDetail":(.*)'
            items = re.compile(regex).findall(html.text)
            items = items.pop()
            items = json.loads(items)
            return items
