#section b.
#number 4.
def employeeBonusCalculations():

    run = 1

    while run == 1:

        salary =  int(input("Enter your salary amount: "))
        yearsOfService =  int(input("Enter your years of service: "))

        if yearsOfService > 4:

            netBonusAmount = int((8/100 * salary))
            
        elif yearsOfService == 3:

            netBonusAmount = int((5/100 * salary))
        else:

            netBonusAmount = 0

        finalPay = salary + netBonusAmount     

        print(f"Your net bonus amount is: {netBonusAmount:,} and your final pay is {finalPay:,}")    

        run = int(input("Press 1 to continue or any number to quit: "))

        if run !=1:
            break


employeeBonusCalculations()


#number 4(b)

def saccoTransactions():

    accountBalance = 0
    run = 1

    while run == 1:

        print("\nWelcome to, WITU Sacco.")

        #items check
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')


        studentChoice = int(input("Enter your selection(1,2,or 3): "))

        # The transactions basing on the student selection

        if studentChoice == 1:

            print('\n...Processing a deposit transaction...')
            depositAmount =  int(input("Enter amount to be deposited: "))

            #checking if deposit amount is less than 1000
            if depositAmount < 1000:

                print('\nMinimum deposit is 1000')

            else:
                accountBalance += depositAmount

                print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')


        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount =  int(input("Enter amount to be withdrawn: "))

            if accountBalance == 0:

                print("Your balance is 0") 

            elif withdrawAmount < 500:

                print("Mininum withdraw amount is 500")

            elif withdrawAmount > accountBalance:

                print(f"Withdraw failed, insufficient funds")

            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')

            
        elif studentChoice == 3:
             print(f'Your account balance is {accountBalance:,}')

            

        else:
            print("You entered  a wrong choice!! Please select 1, 2, or 3\n")


        run = int(input("Enter 1 to continue or any number to exit: "))

        if run!=1:
            print("Thanks for using our sacco")
            break

saccoTransactions()


#number 4(c)
import math

def valueOfD():
    
    X1 = int(input('Enter the value of X1:\t')) 
    X2 = int(input('Enter the value of X2:\t'))
    Y1 = float(input('Enter the value of Y1:\t')) 
    Y2 = float(input('Enter the value of Y2:\t')) 

    simplifiedExpression = (X1-X2) ** 2 + (Y1-Y2) ** 2
    d = math.sqrt(simplifiedExpression)
    #return d
    print("The value of d is: %.2f " %d + " ")
   
#calling the function  
valueOfD()



