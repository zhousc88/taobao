import requests
import re,json
url='https://rate.tmall.com/list_detail_rate.htm?itemId=530487547566&sellerId=2579408925'
html=requests.get(url).text
pat='"rateDetail":(.*)'
items=re.compile(pat).findall(html)
items=items.pop()
items=json.loads(items)
print(items)
com_count=items['paginator']['items']
com_page=items['paginator']['lastPage']
print("评论有%s，有%s页码"%(com_count,com_page))
rates=items['rateList']
for rate in rates:
    userid=rate['id']
    username=rate['displayUserNick']
    content=rate['rateContent']
    ratetime=rate['rateDate']
    rate={'id':userid,'name':username,'content':content,'time':ratetime}
    print(rate)