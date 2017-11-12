import requests
import re,json
url2 ='https://rate.tmall.com/listTagClouds.htm?itemId=522671529510'
html2=requests.get(url2).text
pat='"tagClouds":(.*)}'
items=re.compile(pat).findall(html2)
items=items.pop()
items=json.loads(items)
print(items)
for item in items:
    #item=json.loads(item)
    tag_id=item['id']
    tag_name=item['tag']
    tag_count=item['count']
    tag={'id':tag_id,'tag':tag_name,'count':tag_count}
    print(tag)
