from numpy.random import default_rng
rng = default_rng()
from matplotlib import pyplot as plt
import random as rand

array = rng.choice(a=[False], size=(512,512))

array [333:340,333:340]=True

array [113:220,213:245]=True

print(array)


def ters(intx):
    if intx:
        return False
    if not intx:
        return True
    
def bol(deger):
    if deger:
        return 1
    if not deger:
        return 0

for ar in range (200):
    for i in range(512*512):
        x=i//512
        y=i%512
        if (x < 511) and (y < 511):
            if (x + y) != 0:
                w=bol(array[x,y-1])
                s=bol(array[x,y+1])
                a=bol(array[x-1,y])
                d=bol(array[x+1,y])
                c=bol(array[x,y])
                if c == 1:
                    if w==1 and s==1 and d==0 and a==0:
                        array[x,y]=False
                    if w==0 and s==0 and d==0 and a==0:
                        array[x,y-1]=True
                        array[x,y+1]=True
                        array[x-1,y]=True
                        array[x+1,y]=True
                    if (w+a+s+d)==1:
                        array[x,y]=False
                    if (w+a+s+d)==2 or (w+a+s+d)==3:
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
    fig = plt.figure()
    plt.imshow(array, interpolation='nearest')
    plt.show()
    
    fig.savefig('./Results/1/res_'+str(ar)+'.jpg')