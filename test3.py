from datetime import datetime
class savelog(object):
    def savelog(self,word,word1):
        with open('1.txt','a') as f:
            message = str(datetime.now()) + "  下载了  " + word +" 信息"+word1
            print(message)
            f.write(message+"\n")
            f.close()
if __name__ =="__main__":
    t1=savelog()
    list=['1','2','3','4']

    for li in list:
        print(li)
        t1.savelog(li,"鸡蛋")