import json

def main():
    i = input("Welcom to the Scientists birthday repository! To write, press w! to read press r!")    
    if i.lower() =="w":
        writeJson()

    elif i.lower() =="r":
        x = input("what name are you looking for?")
        getJson(x)

    else:
        print("Error 404")

def writeJson():
    while True:
        name = input("Input a Scientist, or break, to stop and safe: ")
        if name.lower() == "break":
            break
        else:
            birthday = input("Input their Birthday")
            
            data = {
            'Scientists' : [
            {
            'name' : name,
            'birthday' : birthday,            
            }
            ],
            }

    dataJson = json.dumps(data)
    with open("data.txt", "w") as file:
        file.write(dataJson)

def getJson(n):
    dats = open("data.txt", "r")
    print(dats.readline())
    dats.close()





if __name__ == "__main__":
    main()