import csv
from MapTile import*
from AsciiMap import*


A=AsciiMap()
tile=[]
with open('file_test.csv', 'rb') as csvfile:
    mapreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in mapreader:
        j=0
        i=0
        #A.append_row(row)
        arr=[]
        while j < len(row):
            if row[j] is '':
                tile=MapTile(5,5,' ',' ')#create tile object
                #tile.create_tile()
                arr.append(tile)
            else:
                tile=MapTile(5,5,'x',' ')
                #tile.create_tile()
                arr.append(tile)
            j=j+1
        A.append_row(arr)


i=0
B=A.get_row(0)
for tileRow in B[i]:
    j=0
    for tile in tileRow[j]:
        print tile.print_row(j)
        j=j+1
    i=i+1
