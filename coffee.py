import coffee
import main as mn
status = True
def start():
    inpt2 = input("HELP ------------------:- \n"
                "-S -Shutdown,-E -Start :- ")
    inpt2 = inpt2.lower()
    if( inpt2 == "s" ):
        coffee.status = False
    elif(inpt2 == "e"):
        coffee.status = True
    else:
        print("")

while(status is True):

    inpt3 = input("Need a Coffee?? "
          "Enter Y to yes and N to no :- ")
    inpt3 = inpt3.lower()

    if(inpt3 == "y"):
        start()
        mn.begincon
        mn.kook.cook()
        print(f'Milk Stock = {mn.kook.milk} '
              f'Coffee Stock = {mn.kook.rglr_beans} '
              f'Chocolate Stock = {mn.kook.chocolate} '
              f'Dark Coffee stock = {mn.kook.drk_beans} '
              f'Water In Machine = {mn.kook.water} ')
        status = True

    else:
        print("Thank you, You Can Come Again Later :0")
        status = False

