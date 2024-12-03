
def show_balance(balance):
    print("*****************")
    print(f"Your Balance is ₨ {balance:.2f}")
    print("*****************")

def deposit():
    print("*****************")
    amount=float(input("Enter a amount to be deposited: "))
    print("*****************")
    if amount <0:
        print("*****************")
        print("That not a valid amount")
        print("*****************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*****************")
    amount =float(input("Enter you to be withdrawn: "))
    print("*****************")
    if amount> balance:
        print("*****************")
        print("Insuficiant funds")
        print("*****************")
        return 0
    elif amount<0:
        print("*****************")
        print("amoun must be greater than 0")
        print("*****************")
        return 0
    else:
        return amount


def main():
    balance =0
    is_running =True

    while is_running :
        print("*****************")
        print("  BANKING PROGRAM    ")
        print("*****************")
        print("WELCOME .....")
        print("Banking programe")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.exist")
        print("*****************")
        choise = input("Enter your chose(1-4):==> ")

        if choise=='1':
            show_balance(balance)
        elif choise =='2':
            balance += deposit()
        elif choise=='3':
            balance-=withdraw(balance)
        elif choise=='4':
            is_running=False
        else:
            print("*****************")
            print("that not avalid chose")
            print("*****************")
    print("*****************")
    print("THANK YOU ! HAVE A NICE DAY..")
    print("*****************")

if __name__=='__main__':
    main()

