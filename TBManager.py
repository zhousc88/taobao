import requests,re
import json,os,time
import sys
from  datetime import datetime
from Htmlparse import HtmlParser
from StoreData import StoreData
from Dataclean import Dataclean

class DownTaobao(object):
    def __init__(self):
        self.logFile=os.path.join(sys.path[0],"taobao.txt")
        self.dirpath=os.path.join(sys.path[0],"taobao")

    def downdata(self,url,payload):
        items =HtmlParser().html_parser(url,payload)
        img_list,goods_list=Dataclean().goodsclean(items)
        StoreData().store_goods(goods_list)
        paper=items['mods']['pager']['data']
        pape=paper['totalPage']
        print(paper)
        cate_list=Dataclean().clean_category(payload['q'],items)
        StoreData().store_category(cate_list)
        rela_list=Dataclean().clean_related(payload['q'],items)
        StoreData().store_related(rela_list)
        self.downimg(img_list)
        self.down_tag(img_list)
        self.down_rate(img_list)


    def downimg(self,items):
        #下载图片
        if not os.path.exists(self.dirpath):
            print("正在创建图片文件夹")
            os.mkdir(self.dirpath)
        try:
            for item in items:
                html = requests.get(item['url']).content
                filename=os.path.join(self.dirpath,item['id']+".jpg")
                if not os.path.exists(filename):
                    with open (filename,'wb') as fb:
                        print("正在下在%s图片" % item)
                        fb.write((html))
                        fb.close()
                        time.sleep(0.1)
                else:
                    print("%s图片已经存在"%item['id'])
        except Exception as e:
            print("%s异常无法下载"%url)

    def save_log(self,word):
        with open(self.logFile,"a")as fb:
            message=str(datetime.now())+"  下载了  "+word+" 物品信息"
            fb.write(message+"\n")
            fb.flush()

    def down_tag(self,items):
        url="https://rate.tmall.com/listTagClouds.htm"
        for item in items:
            payload={'itemId':item['id']}
            tags=HtmlParser().tag_parser(url,payload)
            tags=Dataclean().tag_clean(tags,item['id'])
            StoreData().store_tags(tags)

    def down_rate(self,items,page=1):
        url='https://rate.tmall.com/list_detail_rate.htm'
        for item in items:
            list=[]
            payload={'itemId':item['id'],'sellerId':item['shopid'],'currentPage':page}
            rates=HtmlParser().rate_parser(url,payload)
            com_count = rates['paginator']['items']
            com_page = rates['paginator']['lastPage']
            rate=Dataclean().rate_clean(rates,item['id'])
            StoreData().store_rate(rate)
            if com_page > page:
                list.append(item)
                self.down_rate(list,page+1)
                time.sleep(0.5)
            else:
                print("评论共有%s条，总共有%s页码" % (com_count, com_page))


if __name__=='__main__':
    url = 'https://s.taobao.com/search'
    payload = {'q': 'python', 'ie': 'utf8', 's': '0'}
       # for i in range(0,100):
       #     payload['s']=i*44
    tb=DownTaobao()
    tb.downdata(url,payload)


