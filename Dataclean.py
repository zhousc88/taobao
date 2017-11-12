#author:zhosuc
import os

class Dataclean(object):

    def goodsclean(self,items):
        imgs=[]
        goods_list=[]
        items = items['mods']['itemlist']['data']['auctions']
        for item in items:
            goods_id = item['nid']
            cate_id = item['category']
            goods_name = item['raw_title']
            pic_url = item['pic_url']
            pic_url = self.url_code(pic_url)
            goods_url = item['detail_url']
            goods_url = self.url_code(goods_url)
            goods_price = item['view_price']
            goods_loc = item['item_loc']
            goods_sales = item['view_sales']
            goods_comment = item['comment_count']
            shop_id = item['user_id']
            shop_name = item['nick']
            shop_code = item['shopcard']['encryptedUserId']
            shop_url = item['shopLink']
            shop_url = self.url_code(shop_url)
            img={'id':goods_id,'url':pic_url,'shopid':shop_id}
            goods = {'id': goods_id, 'cateid': cate_id, 'name': goods_name, 'url': goods_url,
                     'price': goods_price, 'location': goods_loc, 'saled': goods_sales, 'commnent': goods_comment,
                     'shopname': shop_name
                     }
            shops = {'id': shop_id, 'name': shop_name, 'url': shop_url, 'codeid': shop_code
                     }
            goods_li={'goods':goods,'shops':shops}
            goods_list.append(goods_li)
            imgs.append(img)
        return imgs,goods_list

    def clean_category(self,word,items):
        cate_list=[]
        cates = items['mods']['nav']['data']['common']
        cates= cates.pop()
        cates= cates['sub']
        for cate in cates:
            catename=cate['text']
            cateid=cate['value']
            catekey=cate['key']
            cate={'id':cateid,'name':catename,'key':catekey,'word':word}
            cate_list.append(cate)
        return cate_list

    def clean_related(self,word,items):
        rela_list=[]
        items= items['mods']['related']['data']['words']
        for item in items:
            relatedname = item['text']
            relatedurl = item['href']
            relatedurl = "https://s.taobao.com" + relatedurl
            relatedkey = word
            related = {'name': relatedname, 'url': relatedurl, 'key': relatedkey}
            rela_list.append(related)
        return rela_list

    def detail_clean(self, detail):
        # 数据清洗
        detail = detail.replace("<span class=H>", " ")
        detail = detail.replace("</span>", " ")
        return detail

    def url_code(self, url):
        if "https" not in url:
            url = "https:" + url
        return url

    def tag_clean(self,items,word):
        tag_list=[]
        for item in items:
            # item=json.loads(item)
            tag_id = item['id']
            tag_name = item['tag']
            tag_count = item['count']
            tag = {'id': tag_id,'goodsid':word, 'tag': tag_name, 'count': tag_count}
            tag_list.append(tag)
        return tag_list

    def rate_clean(self,items,word):
        items= items['rateList']
        rate_list=[]
        for item in items:
            userid = item['id']
            username = item['displayUserNick']
            content = item['rateContent']
            ratetime = item['rateDate']
            rate = {'id': userid, 'name': username, 'goods':word,'content': content, 'time': ratetime}
            rate_list.append(rate)
        return rate_list
