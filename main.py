class RichBoy(object):
    def __init__(self):
        self.counter=0
        self.s=("Hello")

    def Type(self,st):
        if 0==self.counter:
            self.counter+=1
            return self.s


        if "buy" in st:
            self.s=("Ofc,baby. I'm the richest boy in the world!")
            return self.s
        else:
            self.s=("hey girls...")
            return self.s



class Boy(object):

    def __init__(self):
         self.counter=0
         self.s=("Hello")

    def Type(self, st):
        #self.counter=0
        if 0==self.counter:
            self.counter += 1
            self.s=("Hello")
            return self.s

        if "dress" in st:
            self.s=("U r such a girl! R u afraid of rats?")
            return self.s
        else:
            self.s=("Hey,somebody??")
            return self.s


class Girl(object):
    def __init__(self):
        self.counter=0
        self.s=("Hello")

    def Type(self, st):

        if 0 == self.counter:
            self.counter += 1
            self.s=("Hello")
            return self.s

        if "rats" in st:
            self.s=("AAAAaaa! No! No rats here, pls")
            return self.s
        if 1==self.counter:
            self.s=("I want a dress. Will somebody buy it for me?")
            return self.s

        self.s=("Hey")
        return self.s




def Get_OrderOfUsers():
    Ls=[]
    print("The order of user")
    with open("OrderOfuser.txt","r") as f:
       for line in f:
           Ls.append(line.splitlines())
    return Ls

L=[]
L=Get_OrderOfUsers()
g=Girl()
b=Boy()
r=RichBoy()


s=("hey")
bs=s
for c in range(3):
    s = g.Type(bs)
    gs=s
    print(L[1],":",s)
    s = b.Type(s)
    bs=s
    print(L[0],":",s)
    s=r.Type(gs)
    print(L[2],":", s)