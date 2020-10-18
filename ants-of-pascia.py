from numpy.random import default_rng
rng = default_rng()
from matplotlib import pyplot as plt
import random as rand

array = rng.choice(a=[False], size=(512,512)) #create an blank array with 2 dimension sized 512x512 -> set (a=[False,True] for random array.

array [333:340,333:340]=True #they are optional. 
array [113:220,213:245]=True #they are optional. 

print(array) #for test your array. This is optional too.


def ters(intx): #A function can change false to true and true to false.
    if intx:
        return False
    if not intx:
        return True
    
def bol(deger): #A function can change 1 to 0 and 0 to 1.
    if deger:
        return 1
    if not deger:
        return 0

for ar in range (200): #Main ant loop. 200 moves and 200 images.
    for i in range(512*512): #check size if you want to change size
        x=i//512 #to set 2 cordinates. divide pixel id to screen witdh. This run with loop like: (1,0) (2,0) ... (512,0) (1,512)
        y=i%512 #this give us a one pixel cordinat 
        if (x < 511) and (y < 511): #Borders can be a problem. If pixel id in borders like (244,512) dont process.
            if (x+y) != 0: #dont start for 0,0. I cant remember why i add this.
                w=bol(array[x,y-1]) #set W as pixel up to selected pixels opposite value
                s=bol(array[x,y+1]) #set S as pixel up to selected pixels opposite value
                a=bol(array[x-1,y]) #set A as pixel up to selected pixels opposite value
                d=bol(array[x+1,y]) #set D as pixel up to selected pixels opposite value
                c=bol(array[x,y]) #set W as selected pixels opposite value
                if c == 1: #ONLY if selected pixel TRUE
                    if w==1 and s==1 and d==0 and a==0: #style of ant.
                        array[x,y]=False
                    if w==0 and s==0 and d==0 and a==0: #style of ant.
                        array[x,y-1]=True
                        array[x,y+1]=True
                        array[x-1,y]=True
                        array[x+1,y]=True
                    if (w+a+s+d)==1: #style of ant.
                        array[x,y]=False
                    if (w+a+s+d)==2 or (w+a+s+d)==3: #style of ant.
                        array[x,y-1]=ters(array[x,y-1])
                        array[x,y+1]=ters(array[x,y+1])
                        array[x-1,y]=ters(array[x-1,y])
                        array[x+1,y]=ters(array[x+1,y])
                # else:
                #     w=ters(w)
                #     a=ters(a)
                #     s=ters(s)
                #     d=ters(d)
                #     if w==1 and s==1 and d==1 and a==1:
                #         array[x,y]=0
                #     if w==0 and s==0 and d==0 and a==0:
                #         array[x,y-1]=1
                #         array[x,y+1]=1
                #         array[x-1,y]=1
                #         array[x+1,y]=1
                #     if (w+a+s+d)==1:
                #         array[x,y]=0
                #     if (w+a+s+d)==2 or (w+a+s+d)==3:
                #         array[x,y-1]=ters(array[x,y-1])
                #         array[x,y+1]=ters(array[x,y+1])
                #         array[x-1,y]=ters(array[x-1,y])
                #         array[x+1,y]=ters(array[x+1,y])
                
    fig = plt.figure() #set a plot
    plt.imshow(array, interpolation='nearest') #set this array to image
    plt.show() #show image
    
    fig.savefig('./Results/1/res_'+str(ar)+'.jpg') #save images for 200 times.
