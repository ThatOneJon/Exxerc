import math
import re
from operator import itemgetter, attrgetter

class gen:
    def itr(self,  s ):
        self.s = s
        for i in range(0, s+1):
            if i%7 == 0:
                yield i     
            else:
                continue

class american:

    @staticmethod
    def americano():
        print("Nationality: Americano!")


class newYorker(american):
    ...


class tre:
    def __init__(self, aparam):
        self.aparam = aparam


    def x (self):
        return(self.aparam)


class circle:
    def __init__(self, r):
        self.r = r
        self.circ = self.r**2 * math.pi

    @property
    def getcirc(self):
        return self.circ



def main():
    #qeight()
    #q19()
    #q20()
    #q21()
    #q22()
    #q23()
    #q24()
    #q25()
    #q26()
    #q27()
    #q28()
    #q30()
    q31()
    qamerican()

def qeight(): 
    sentence = input("Enter your password!")
    if len(sentence) >= 6 and len(sentence) <= 12:
        if re.search("[a-z]+",sentence):
            if re.search("[A-Z]+", sentence):
                if re.search("[0-9]+", sentence):
                    if re.search("[$#@]+", sentence):
                        print("valid")
                    else:
                        print("invalid")
        else:
            print("Requirements not fulfilled!")
    else:
        print("length between 6 and 12 characters")




def q19():
    listofT = []
    while True:
        if tup := input("your tuple"):
            tup_x = ()
            for _ in tup.split(","):
                #concatonate tuple???????
                tup_x = tup_x + (_,)
            listofT.append(tup_x)
        else:
            break
    listofT = sorted(listofT, key = itemgetter(0,1,2))

    print(listofT)


def q20():
    x =gen()
    i = x.itr(30)
    print(list(i))


def q21():
    ...

def q22():
    x = input("Input the sentence!").split(" ")
    fins = {}

    for _ in x:
        count = 0
        for _ in x:
            count += 1
            fins[_] = count

    words = sorted(fins, key = lambda x : x[0])

    for word in words:
        print(f"{word} : {fins[word]}")


def q23():
    x = int(input("A number"))
    print(x**2)


def q24():
    print(abs.__doc__)
    print(int.__doc__)

def q25():
    i = tre(80)
    print(i.x())


def q26():
    li = []
    for i in range(0,2): 
        li.append(input("str:  "))

    l1 = len(li[0])
    l2 = len(li[1])

    if l1 > l2:
        print(li[0])
    elif l2 > l1:
        print(li[1])
    else:
        print(li[0], li[1])

def q27():
    dick = {}
    lis = []
    for i in range(0, 20 +1):
        dick[i] = i**2
        lis.append(i**2)
    for _ in range(0, 5):
        print(lis[_])

    for j in range(len(lis)-5, len(lis)):
        print(lis[j])

    for h in range(5, len(lis)):
        print(lis[h])


    print(dick)

def q28():
    tub = (1,2,3,4,5,6,7,8,9,10)
    x = int(len(tub)/2)
    for i in range(0, x):
        print(f"{tub[i]}, ", end ="")

    print("\n")
    for j in range(x, len(tub)):
        print(f"{tub[j]}, ", end ="")

    print("\n")
    tp=(1,2,3,4,5,6,7,8,9,10)
    tp1=tp[:5]
    tp2=tp[5:]  
    print (tp1)
    print (tp2)


def q30():
    c = (1,2,3,4,5,6)
    for y in c:
        if y%2 == 0:
            print(y)
        else:
             continue

    l =  [1,2,3,4,5,6,7,8,9,10]
    l = filter(lambda a :  a%2 == 0 , l)
    print(list(l))

    k = [1,2,3,4,5,6,7,8,9,10]
    res = map(lambda x : x**2 ,k)
    print(list(res))

def q31():
    li = [1,2,3,4,5,6,7,8,9,10]
    print(list(filter(lambda y : y%2 == 0 ,map(lambda x : x**2, li))))
    print(list(filter(lambda z : z%2 == 0, range(0,21))))
    print(list(map(lambda w : w**2, range(0, 21))))

def qamerican():
    american.americano()
    newYorker.americano()
    c = circle(3)
    print(c.getcirc)


if __name__ == "__main__":
    main()