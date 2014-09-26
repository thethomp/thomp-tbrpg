class MapTile:

    def __init__(self,xdim,ydim,perchar,inchar):
        self.xdim=xdim
        self.ydim=ydim
        self.perim = perchar
        self.inside= inchar
        self.tile = []

        self.create_tile()#load up tile, no reason to call create_tile()?? for each

    def get_xdim(self):
        return self.xdim

    def get_ydim(self):
        return self.ydim

    def get_cell(self,num1,num2):
        return self.tile[num1][num2]

    def create_tile(self):
        x=self.xdim
        y=self.ydim
        lst=[]
        for num in range(0,y):
            if num in (0,y-1):
                self.tile.append(self.perim*x)
            else:
                self.tile.append(self.perim +
                                 self.inside*(x-2) +
                                 self.perim)

    def print_tile(self):
        print self.tile

    def print_row(self,num):
        print self.tile[num]
	
    def get_tile(self):
	return self.tile
