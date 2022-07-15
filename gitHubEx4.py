import re

class rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def calc(self):
        return self.x * self.y

class shape:
    def __init__(self):
        self.area = 0


class square(shape):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def arr(self):
        self.area = self.x * self.y
        return self.area



class customEx(Exception):
    def __init__(self, s):
        self.s = s



class generator():

    def nums(self, x):
        i = 0
        while i < x:
            if i%2 == 0:
                yield i
            i += 1



def main():
    #q1()
    #q2()
    #q3()
    #q4()
    #i = input("n ")
    #for _ in genrateur(i):
     #   print(_)

    evals()

def q1():
    rect = rectangle(10, 4)
    print(rect.calc)
    x = square(10,2)
    print(x.arr)

def q2():
    x = customEx("An error")
    print(x)
    try:
        raise x
    except customEx:
        print(x)


def q3():
    x = "username@companyname.com"
    name = re.match(r"(\w*\W*)@(\w+\.)", x)
    print(name[1])
    print(name[2])



def q4():
    x = generator()
    for _ in x.nums(11):
        print(_)

def genrateur(n):
    for _ in range(0, int(n) + 1):
        if _%7 == 0 and _%5 == 0:
            yield _

def evals():
    y = input("Expression!")
    print(eval(y))

    lis = [9, 8, 99, 9,9, "all", "allllllsss"]
    c = input("search: ")
    print(lis.index(c))


if __name__ == "__main__":
    main()