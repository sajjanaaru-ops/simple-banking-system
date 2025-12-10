import time as tm
#for users who clone my repo. to initialize the database for them
with open('customer_data.txt','w') as f:
    if f:
        pass
    else:
        f.write('{}')#this should initializes the database 
        
class BankAccount:
    def __init__(self,balance,file_path,name):
        self.__balance=balance
        self.file=open(file_path,'r')
        self.data=eval(self.file.read())
        self.name=name
        self.file.close() 
    #getter for the balance
    def get_balance(self):
        print(f'CURRENT BALANCE:{self.__balance}')
    #setter for the balance
    def deposit(self,money):
        self.money=money
        self.__balance+=self.money
        self.data[f'{name}-Balance']=self.__balance
        f=open(file_path,'w')
        f.write(str(self.data))
        f.close() 
        print(f'added {money} to the acoount \npresent balance: {self.__balance}')
    #to remove money from the account
    def remove(self,amount):
        self.amount=amount
        self.__balance-=self.amount
        self.data[f'{name}-Balance']=self.__balance
        f=open(file_path,'w')
        f.write(str(self.data))
        f.close() 
        print(f'withdrawed:{amount}\nremaining balance:{self.__balance}')


class Customer_data:
    def __init__(self,file_path,name,password):
        self.file=open(file_path,"r")
        self.data=eval(self.file.read())
        self.password=password
        self.n=0
        self.p=0
        self.var=True
        if name in self.data.keys():
            self.n=1      
            if self.password==self.data[name]:
                self.p=1
            else:
                print('incorrect password\nRedo-do the login')
                self.var=False
        else:
            print("User doesn't exists")
        if self.n==1 and self.p==1:
            print('successfully Verified')            
    def verification(self):
        if self.n==1 and self.p==1:
            return True
        else:
            return False
    def Balance(self):
        bal=self.data[f'{name}-Balance']
        return bal
class Data_Mod:
    def __init__(self,file_path):
        self.file=open(file_path,'r')
        #extracting the data
        self.data=eval(self.file.read())#this has the dictionary loaded from the file
        self.var=True

    def new_user(self,name,password):
        self.name=name
        self.password=password
        if name not in self.data.keys():
            self.data[self.name]=self.password
            self.data[f'{name}-Balance']=deposit
            f=open(file_path,'w')
            f.write(str(self.data))
            f.close()
            self.var=False
            print(f'New User Successfully added.\nWelcome to the banking system, {name}')
        else:
            print('The User Already Exists')

    def change_password(self,name,password,new_password):
        self.name=name
        self.password=password
        self.new_password=new_password
        if name in self.data.keys():
            if self.data[name]==self.password:
                self.data[name]=self.new_password
                f=open(file_path,'w')
                f.write(str(self.data))
                f.close()
                self.var=False
                print('Password successfully changed!')
            else:
                print('incorrect password')
        else:
            print("user doesn't exist")
            

     
file_path='C:/Users/sajja/OneDrive/Desktop/python/basic banking system/customer_data.txt'
check=0
print("Welcome to the banking service system\nNOTE:THE ENTIRE SYSTEM IS CASE-SENSITIVE")
while check!=100:
    print('1.lOGIN\n2.NEW USER REGISTRATION\n3.CHANGE PASSWORD\n4.EXIT')
    check=int(input('Please Enter your choice\n'))
    match check:
        case 1:#login
            name=input('enter name\n')                
            password=input('enter password\n')
            user=Customer_data(file_path,name,password)
            if user.verification():
                bal=user.Balance()
                user_acc=BankAccount(bal,file_path,name)
                choice=7
                while choice!=4:
                    print('1.CHECK BALANCE\n2.ADD MONEY \n3.WITHDRAW\n4.LOGOUT')
                    choice=int(input('enter the choice\n'))
                    match choice:
                        case 1:
                            user_acc.get_balance()
                            tm.sleep(2)
                        case 2:
                            money=int(input('enter the amount you want to deposit\n'))
                            user_acc.deposit(money)
                            tm.sleep(2)   
                        case 3:
                            money=int(input('enter the amount you want to withdraw\n')) 
                            user_acc.remove(money)
                            tm.sleep(2)    
                        case 4:
                            print('thank you for using our services')
                        case _:
                            print('Invalid Choice')
                            tm.sleep(2)   
        case 2:#new user  
            user=Data_Mod(file_path)
            while user.var:
                name=input('enter the username\n')
                password=input('enter the password\n')
                re_password=input('Re-Enter the password\n') 
                tick=True
                while tick:
                    if password==re_password:
                        user.new_user(name,password)
                        deposit=int(input('enter the initial deposit\n'))
                        tick=False
                    else:
                        print('the passwords didnt match')
                        password=input('enter the password\n')
                        re_password=input('Re-Enter the password\n')
            tm.sleep(2)

        case 3:#changing password
            user=Data_Mod(file_path)
            while user.var:
                name=input('enter the username\n')
                password=input('enter the current password\n')
                new_password=input('Enter the new password\n')
                user.change_password(name,password,new_password)
            tm.sleep(2)

        case 4:#exit
            check=100
            print('Thank You for using our services.\nHope you had good experience')
            tm.sleep(2)
                





                        





                    







                        