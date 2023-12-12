import sqlite3
import random as r
# Create account
# Open Account
class Bank:
    print("WELCOME TO THE BANK")
    def __init__(self):
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        print("Sqlite3 Connected")


    def createAccount(self):
        self.c.execute("""create table if not exists Bank   (
            
            account_name text,
            account_num integer,
            balance integer

        )""")

        # self.c.execute("drop table Bank")

        n1 = input("Enter Your Name:-  ").upper()
        n2 = input("Enter your Second Name:-  ").upper()
        
        if n1.isalpha() and not n1.isspace() and  n2.isalpha() and not n2.isspace():
            name = n1+ ' ' +n2
            num = r.randint(10000000, 99999999)
            amount = 0
            self.c.execute(" insert into Bank values(?,?,?)", (name, num, amount))
            print("{} Your Account Got Created Successfully.......! ".format(name))
            print("Please Note Down Your Account Number:-  {}". format(num))
            self.con.commit()
            self.c.execute(" select * from Bank")
            print(self.c.fetchall())
            self.con.close()
        else:
            print("Enter valid Name, Try Again..............")



    def OpenAccount(self):
        a_num = int(input("Enter Your Account Number:-  "))
        check = True
        flag = False
        for a,b,c in self.c.execute("select * from Bank"):
            if b == a_num:
                check = False
                flag = True
                val = c
                na = a

                print("(D) - Deposit")
                print("(W) - Withdraw")
                print("(C) -  Check Balance")

                ope = input("Enter any of the operation (C)/(D)/(W) :-  ")


        if flag and (ope == 'd' and 'D'):
            dep = int(input("Enter The Amount To Deposit:-  "))
            deposit = dep + val
            self.c.execute(" update Bank set balance = ? where account_num = ? ", (deposit, a_num))
            self.con.commit()
            print("Amount Deposited {}  ₹, Available Balance is {}  ₹".format(dep,deposit))
            self.c.execute(" select * from Bank")
            print(self.c.fetchall())
            
        
        if flag and (ope == 'w' or ope == 'W'):
            wit = int(input("Enter the amount to withdraw:-  "))
            if val > 0  and val >= wit:
                withdraw_bal = (val - wit)
                self.c.execute("update Bank set balance = ? where account_num = ?", (withdraw_bal, a_num))
                self.con.commit
                print("Withdraw  {} ₹, done successfully......! Available balance {} ₹".format(wit, withdraw_bal))
                self.c.execute(" select * from Bank")
                print(self.c.fetchall())
                
            else:
                print("Low Balance")


        if flag and (ope == 'c' or ope == 'C'):
            print("Hello {}, Your Account Balance is {} ₹ ".format(na,val))

        if check:
            print("Invalid Account Number.......!")


bk = Bank()

print("(C) -> Create Account")
print("(O) -> Open Account")
op = input("Enter Your Choice (C)/(O):-  ")

if op == 'C' or op == 'c':
    bk.createAccount()

elif op == 'O' or op == 'o':
    bk.OpenAccount()


