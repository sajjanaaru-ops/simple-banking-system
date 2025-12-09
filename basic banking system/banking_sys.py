class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    #getter for the balance
    def get_balance(self):
        print(self.__balance)
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
        self.file_path=file_path
        self.name= name
        self.password=password
        self.n=0
        self.p=0
        with open(file_path,'r') as data:
            for i in data:
                l=eval(i)
                if self.name == l[0]:
                    print('name is in database')
                    self.n=1
                else:
                    print('name is not in database')
        with open(file_path,'r') as data:
            for i in data:
                l=eval(i)        
                if self.password==l[1]:
                    print('the password is correct')
                    self.p=1
                else:
                    print('incorrect password')
        if self.n==1 and self.p==1:
            print('successfully verified')
        else:
            print('incorrect name/password')
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
            case _:
                print('invalid choice')   





                    







                        