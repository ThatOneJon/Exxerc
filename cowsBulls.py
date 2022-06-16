import random
def main():
    print("Welcome to cows and bulls game!")
    number = []
    for _ in range(4): 
        x = random.randrange(0,9)
        number.append(x)
    cowsBulls(number)


def cowsBulls(i):   
    tryCounter = int()

    cows = 0
    bulls =  0

    while cows != 4:
        cows = 0
        bulls =  0

        inp = input("Whats your 4 digit number?")
        tryCounter += 1
        if len(inp) == 4:
            for _ in inp: 
                if int(_) in i:
                    cows += 1

                else:
                    bulls +=1
            
            print(f"you got: cows {cows} and bulls {bulls}")

        else:
            print("idiot 4 digits F O U R !")

    print(f"congrats you took {tryCounter} tries")





if __name__ == "__main__":
    main()