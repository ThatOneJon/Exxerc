class calculator:
    def __init__(self, id):
        self.id = id

    def addition(self,x,y):
        return x + y



    def subtraction(self,x,y):
        return x - y


    def division(self,x,y):
        try:
            return x/0

        except ZeroDivisionError :
            return "error"

    def multiply(self,x,y):
        return x * y



def main():

    x = calculator(9883)
    print (x.id)
    print(x.addition(2, 3))
    print(x.division(2,0))
    print(x.multiply(2,3))




if __name__ == "__main__":
    main()