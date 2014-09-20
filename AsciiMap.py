from MapTile import *

class AsciiMap(object):
    
    def __init__(self):
        self.arr = []
        
    def append_row(self,row):
        self.arr.append(row)
        
    def get_row(self,num):
        if num < len(self.arr):
            return self.arr[num]
        else: print "invalid index"

    def get_rowlen(self,num):
        if num < len(self.arr):
            return len(self.arr[num])
        else: print "invalid index"
