import re # for regular expr.

def findWholeWord(w):
    """Regular expression for finding a word in a string.
    Word should be around spaces."""

    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


class RichBoy(object):
    """Rich Boy object.It has method type(), which return a needed string.
    getName()- get a name from a object made by my hands"""

    def __init__(self):
        self.counter=0      # for the first phrase 'Hello'

        # the common string for returning the comment.
        #I just called it on a default mode
        self.s=("Hello")

    def Type(self,st):
        """Method for returning a string into a chat.
        The first phrase is always 'Hello' """

        if 0==self.counter:
            self.counter+=1
            return self.s   #return 'Hello'

        if "buy" in st:     #if in st is 'buy' return the string below "ofc,baby...."
            self.s=("Ofc,baby. I'm the richest boy in the world!")
            return self.s
        else:               #Else return another string
            self.s=("hey girls...")
            return self.s

    def getName(self):
        """Return the name of the object"""
        return "RichBoy"


#All comments, which are higher, can also correlate to another classes ,I mean about: Boy, Girl.
#That's why dont comment them




class Boy(object):
    """Boy object.It has method type(), which return a needed string.
        getName()- get a name from a object made by my hands"""

    def __init__(self):
         self.counter=0
         self.s=("Hello")

    def getName(self):
        return "Boy"

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
    """Girl object.It has method type(), which return a needed string.
            getName()- get a name from a object made by my hands"""
    def __init__(self):
        self.counter=0
        self.s=("Hello")

    def getName(self):
        return "Girl"

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




def MainFunction():
    """main function"""
    c=0               #Counter for counting the size of a list of name users
    Ls=[]                   #Empty list
    gstr="Girl"         #The string is on default for print 137 line and etc.And redefine it in 117
    bstr="Boy"
    rstr="RichBoy"

    print("The order of user")
    with open("OrderOfuser.txt","r") as f: # read from a file
        for line in f:
            Ls.append(line.splitlines())    # splitlines helps me for taking a string from a file without '\n'

            if  findWholeWord(gstr)(line):  #use r.expression
                g = Girl()                  #if it's ok. Create and object
                c+=1                  #size plus one
                gstr=g.getName()            # getting Name for gstr

            elif findWholeWord(bstr)(line):
                b = Boy()
                c+=1
                bstr=b.getName()

            elif findWholeWord(rstr)(line):
                r = RichBoy()
                c+=1
                rstr=r.getName()


    s=("hey")                       #The string for type method
    bs=s
    ListSize=c

    for f in range(ListSize):       #till listsize under counter
        s = g.Type(bs)
        gs=s
        print(gstr,":",s)           #print a comment
        s = b.Type(s)
        bs=s
        print(bstr,":",s)
        s=r.Type(gs)
        print(rstr,":", s)


MainFunction()