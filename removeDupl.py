def main():
    lista = [22, 30, 10, 5, 7, 8]
    listb = [30, 50 ,8 , 9, 3, 2]
    print(remove(lista, listb))
    try:
        x = int(input("give a number !"))
    except ValueError:
        print("The input has to be a whole number!")

    print(isInList(x, lista))



def remove(a, b):
    result = list()
    for _ in a:
        if _ in b:
            result.append(_)

    return result

def isInList(c, a):
    if c in a:
        return True
    else:
        return False







if __name__ == "__main__":
    main()