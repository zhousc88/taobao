#author:zhousc
import pickle
class GManager(object):
    def __init__(self):
        self.new_goods=self.load_progress("new_goods.txt")
        self.old_goods=self.load_progress("old_goods.txt")

    def has_new_goods(self):
        return len(self.new_goods) != 0

    def add_new_goods(self,goods):
        if goods is None or len(goods) ==0:
            return
        if goods not in self.new_goods and goods not in self.old_goods:
            self.new_goods.add(goods)

    def get_new_goods(self):
         new_goods=self.new_goods.pop()
         self.old_goods.add(new_goods)
         return new_goods

    def save_progress(self,path,data):
        with open(path,'ab') as f:
            pickle.dump(data,f)

    def load_progress(self,path):
        try:
            with open(path,'rb')as f:
                tmp=pickle.load(f)
                return tmp
        except:
            print("无进度文件，创建%s"%path)
        return  set()
