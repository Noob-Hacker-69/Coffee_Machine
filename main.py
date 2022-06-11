import time
import prettytable as P
import c1art
#MENU LIST
Id = [0, 1, 2, 3, 4, 5, 6, 7]
limst1 = ["black coffee", "capatinno", "robesta", "arabica", "liberica", "koa coffee", "blue mountain coffee", "chocolate coffee"]
Price = [1.5, 2, 1.25, 1.75, 2.5, 3.0, 3.25, 2.75]

table = P.PrettyTable()

table.add_column("Id", Id)
table.add_column("coffee Names", limst1)
table.add_column("Comst(usd-$)", Price)
# PRINTING TABLE
print(table)
class begin():
    def Return(self):
        self.req = int(input("select from these and enter the id number of item:- "))
        self.cost = Price[self.req]
        print(f'The Price Of Your Coffee Please {self.cost}')
        self.inpt = int(input("insert coins:- "))
        if (self.cost == self.inpt):
            print("THANK YOU FOR PERFECT CHANGE :)")
            return True
        elif (self.cost > self.inpt):
            print("SORRY NEED TO INSERT MORE MONEY :(")
            return False
        else:
            back = self.inpt-self.cost
            print()
            print(f" PLEASE COLLECT YOUR CHANGE BACK :) {back}")
            return True
begincon = begin()

#chef for brewing coffee
class chef():
    def __init__(self):
        self.chocolate    = 10
        self.rglr_beans   = 100
        self.drk_beans    = 100
        self.water        = 1000
        self.milk         = 1000

    def cook(self):
        stock = True
        if (begincon.Return() is True):
            if(self.chocolate <=1 or self.rglr_beans <= 10 or self.drk_beans <= 10 or self.water <=50 or self.milk <=100):
                stock = False
            if(stock is False ):
                print("WAIT FOR FEW SEC'S WE ARE OUT OF STOCK :| ")
                for i in range (1,6):
                    time.sleep(5)
                    print(i*"0")
                self.chocolate = self.chocolate+10
                self.rglr_beans = self.rglr_beans+10
                self.drk_beans = self.drk_beans+10
                self.water = self.water+1000
                self.milk = self.milk+1000

            print("YOUR COFFEE IS STARTED BREWING WAIT FOR FEW SEC'S :) ")
            #loading animation
            for i in range(1,6):
                time.sleep(3)
                print(i*"~")

            if(begincon.req == 7):
                self.chocolate = self.chocolate - 1
                self.milk = self.milk - 100
                self.water = self.water - 50
            elif(begincon.req == 0 ):
                self.drk_beans = self.drk_beans - 10
                self.milk = self.milk - 100
                self.water = self.water - 50
            else:
                self.drk_beans = self.rglr_beans - 10
                self.milk = self.milk - 100
                self.water = self.water - 50
            print("TAKE YOUR CUP OF COFFEE THANK YOU VISIT AGAIN :)")
            time.sleep(2)
            if (begincon.req==5):
                c1art.draw1()
            elif (begincon.req==6):
                c1art.draw1()
            else:
                c1art.draw2()

        else:
            print("YOUR PAYMENT ISN'T DONE YET :(")

kook = chef()
