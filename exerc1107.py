import random
import math
import datetime
import calendar
import socket
import re


def main():
    #beerSong()
    #dnD()
    #change()
    #duplicate()
    #print(morseCode())
    #print(friday())
    #print(DNSReq())
    #print(parseStr())
    #print(hexa())
    #revInt()
    #average()
    #print(conv_Add())
    #print(param_Count(3, 4, 5))
    #print(xOR())
    #print(countXO())
    #print(creditCard())
    print(doubleString())

def beerSong():
    for i in range(1, 100):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer. \n Take one down and pass it around, {i} bottles of beer on the wall.")

def dnD():
    skills = {
        "strength" : 0,
        "dexterity" : 0,
        "constitution" : 0,
        "int" : 0,
        "wisdom" : 0,
        "charisma" : 0
    }
    key_list = list(skills)

    for _ in key_list:
        nums = []
        for i in range(0, 4):
            x = random.randrange(0, 7)
            nums.append(x)
        nums.remove(min(nums))
        skills[_] = sum(nums)

    hitpoints = 10 + math.floor((skills["constitution"]-10)/2)

    print(f"your character has: {hitpoints} hitpoints! ")
    for c in skills:
        print(f"{c}: {skills[c]}")


def change():
    coins = [10, 20, 5, 15, 1, 20]
    changeAmount = int(input("How much is the change? "))

def duplicate():
    i = input("A sentence:  ").split(" ")
    for _ in i:
        j = list(_)

        if len(set(j)) != len(j):
            print(f"Duplicate letter in word: {_}")
            break

        else:
            continue

def morseCode():
    alphabet = {"a" : "· -", "ä" : " · - · -", "b" : "- · · ·", "c" : "- · - ·",
    "ch" : "- - - -", "d" : "- · ·", "e" : "·", "f" : "· · - ·", "g" : "- - ·",
    "h" : "· · · ·", "i" : "· ·", "j" : "· - - -", "k" : "- · -", "l" : "· - · ·",
    "m" : "- -", "n" : " - ·", "o" : "- - -", "ö" : "- - - ·", "p" : "· - - ·",
    "q" : "- - · -", "r" : "· - ·", "s" : "· · ·", "t" : "-","u" : "· · -",
    "ü" : "· · - -", "v" : "· · · -", "w" : "· - -", "x" : "- · · -",
    "y" : "- · - -",
    "z" : "- - · ·"	
    }
    translated = list()
    sent = input("To translate! \n").lower().split()
    for _ in sent:
        for i in list(_):
            translated.append(alphabet[i])            
        translated.append("----new word-----")
    return "\n".join(translated)


def friday():
    date = input("Input a month and a year, separated by /!    ").split("/")
    days = calendar.monthrange(int(date[1]),int(date[0]))[1]

    for _ in range(1,days):

        day = datetime.datetime(int(date[1]),int(date[0]), _ )
        weekday = day.strftime("%A")

        if weekday == "Friday" and _ == 13:
            return "Friday 13th!!!"
        else:
            continue
    return("No Friday 13th!!")


def DNSReq():
    IP = input("Input an IP Adress!")
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if(re.search(regex, IP)):
        return(socket.gethostbyaddr(IP))

    else:
        return("Not valid ip") 


def parseStr():
    inp = input("Name, ID:  ")
    regex = r"([a-zA-Z]+)(?:0+)([a-zA-Z]+)(?:0+)(\d+)"
    data = re.match(regex,inp)
    return f"First Name: {data[1]}  \nName: {data[2]} \nID: {data[3]}"


def hexa():
    inp = int(input("Decimal:  "))
    return hex(inp)


def revInt():
    i = int(input("NUMBER:  "))
    li = list(str(i))
    li.reverse()
    li = int("".join(li))
    print(li)

def average():
    lis = [10, 15, 5]
    length = len(lis)
    print(round((sum(lis) / length), 3))
    print(max(lis), min(lis))
    liso = lis
    liso.reverse()
    print(liso)
    print(liso + lis)

    lis.remove(max(lis))
    print(max(lis))


def conv_Add():
    i = int(input("A number!"))
    if i > 0:
        numbers = "{:,}".format(i)
        return str(numbers)

    else:
        return ("only positive ints")


def param_Count(*args):
    arguments = list(args)
    return len(arguments)

def xOR():
    list1_xor = [1, [1, 2, 3], [4, 5, 6, 1]]
    if (list1_xor[0] in list1_xor[1]) ^ (list1_xor[0] in list1_xor[2]):
        return True

    else:
        return False


def countXO():
    sentence = input("A sentence, which has X and O!").replace(" ", "").lower()
    
    X = len(list(filter(lambda i : i == "x",sentence)))
    O = len(list(filter(lambda y : y == "o", sentence)))

    return f"number of X: {X} \nnumber of O: {O}"

def creditCard():
    number = 44432333334
    numberFin = ""
    for _ in range(0, len(str(number)) - 4):
        numberFin = numberFin + "*"

    for i in range(len(str(number))-4, len(str(number))):
        numberFin = numberFin + str(number)[i]

    return f"Your credit Card number:  {numberFin}"


def doubleString():
    string = input("A String: ")
    return "".join(list(map(lambda i : i*2, string)))





if __name__ == "__main__":
    main()