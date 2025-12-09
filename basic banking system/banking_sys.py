class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    #getter for the balance
    def get_balance(self):
        print(f'CURRENT BALANCE:{self.__balance}')
    #setter for the balance
    def deposit(self,money):
        self.money=money
        self.__balance+=self.money 
        print(f'added {money} to the acoount \npresent balance: {self.__balance}')
    #to remove money from the account
    def remove(self,amount):
        self.amount=amount
        self.__balance-=self.amount
        print(f'withdrawed:{amount}\nremaining balance:{self.__balance}')    
class Customer_data:
    def __init__(self,file_path,name,password):
        self.file=open(file_path,"r")
        self.data=eval(self.file.read())
        self.password=password
        self.n=0
        self.p=0
        if name in self.data.keys():
            self.n=1      
            if self.password==self.data[name]:
                self.p=1
            else:
                print('incorrect password\nRedo-do the login')
        else:
            print("User doesn't exists")
        if self.n==1 and self.p==1:
            print('successfully Verified')            
    def verification(self):
        if self.n==1 and self.p==1:
            return True
        else:
            return False
                
file_path='C:/Users/sajja/OneDrive/Desktop/python/basic banking system/customer_data.txt'
name=input('enter name\n')                
password=input('enter password\n')
user=Customer_data(file_path,name,password)
if user.verification():
    bal=int(input('enter initial balance'))
    user_acc=BankAccount(bal)
    choice=7
    while choice!=4:
        print('1.GET BALANCE\n2.ADD MONEY \n3.WITHDRAW\n4.LOGOUT')
        choice=int(input('enter the choice'))
        match choice:
            case 1:
                user_acc.get_balance()
            case 2:
                money=int(input('enter the amount you want to deposit'))
                user_acc.deposit(money)   
            case 3:
                money=int(input('enter the amount you want to withdraw')) 
                user_acc.remove(money)    
            case 4:
                print('thank you for using our services')
            case _:
                print('invalid choice')   





                    







                        