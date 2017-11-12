#author:zhousc
import pickle
class GManager(object):
    def __init__(self):
        self.new_goods=self.load_progress("new_goods.txt")
        self.old_goods=self.load_progress("old_goods.txt")


