from os import listdir, getcwd


# Creating Data file if not exist 
if 'Data' not in listdir(getcwd()):
    with open("Data", 'w') as f:
        pass

Data = {}


# Loading Data file 
with open("Data", 'r') as f:
    k = f.read()
    if k=="":
        pass
    else:
        Data = eval(k)


while True:
    options = int(input("\n1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. Check Balance\n5. Exit\n\n"))
    
    if (0<options<6):
        
        # Exit 
        if options==5:
            print("Thank You for banking with Us!")
            break
        # Account Creation   
        if options == 1:
            account = int(input("Enter a Account number: "))
            
            if account in Data.keys():
                print(account, " is already Exist")
            else:
                bal = int(input("Enter intial Amount: "))
                if bal>0:
                    Data[account] = bal
                    print("Your Account Number is Created: ", account, " with initial balance: ", bal)
                else:
                    print("Amount should be greater than 0")
        
        # Deposit Money
        if options == 2:
            account = int(input("Enter Your Account Number: "))
            
            if account in Data.keys():
                amt = int(input("Enter Deposit Amount: "))
                Data[account] += amt
                print("Deposite Successfull! \nYour Current balance: ", Data[account])
            else:
                print("Account Not Exist!")
            
        # Withdraw Money     
        if options == 3:
            account = int(input("Enter Your Account Number: "))
            
            if account in Data.keys():
                Wamt = int(input("Enter Withdraw Amount: "))
                if (Data[account]>=Wamt):
                    Data[account] -= Wamt
                    print("Withdrawl Successfull! \nYour Current balance: ", Data[account])
                else:
                    print("Low Balance! Your balance: ", Data[account])
            else:
                print("Account Not Exist!")
        
        # Checking Balance 
        if options == 4:
            account = int(input("Enter Your Account Number: "))
            
            if account in Data.keys():
                print("Yout Current Account Balance: ", Data[account])
            else:
                print("Account Not Exist!")
                
    else:
        print("Enter a valid Option!!!\n")
    

# Updating Data file 
with open("Data", 'w') as f:
    f.write(str(Data))
    print("\nFile Updated!")