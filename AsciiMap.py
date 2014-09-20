from MapTile import *

class AsciiMap(object):
    
    def __init__(self):
        self.arr = []
        
    def append_row(self,tile):
        self.arr.append(tile)

    def get_tile(self,num):
        if num < len(self.arr):
            return self.arr[num]
