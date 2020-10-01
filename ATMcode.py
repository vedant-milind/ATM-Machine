class atm:
    def __init__(self,name):
        self.name=name
    def acc_info(self):
        print('Account Information: ')
        print('Name: ', name, end='\n')
        print('Account Number: ', info[name][0], end='\n')
        print('Phone Number: ', info[name][1], end='\n')
    def pin_change(self):
        i=3
        while(i>0):
            p=int(input('Enter Original PIN: '))
            if p==info[name][2]:
                x=input('Enter New PIN: ')
                info[name][2]=x
                break
            else:
                i=i-1
                print('PIN incorrect, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
    def acc_balance(self):
        print('Account Balance: ',info[name][3])
    def withdraw(self):
        print('Account Balance: ',info[name][3])
        amt=float(input('Enter Amount To Be Withdrawn: '))
        if amt<=info[name][3]:
            info[name][3]=info[name][3]-amt
            print('New Account Balance is : ', info[name][3])
        else:
            print('Insufficient Balance in Account!')
    def deposit(self):
        amt=float(input('Enter Amount To Be Deposited: '))
        info[name][3]=info[name][3]+amt
        print('New Account Balance: ', info[name][3])

info={"ABC":[4612485411,123454562,4545,12000.00], "DEF":[3769845253,1234567895,8989,10000.00], 'Vedant':[4324567890,1122334455,1234,100000.00], "ATH":[6669857142,12345677412,1111,17000.00], "XYZ":[7779848475,123458481,7777,10500.00]}
k=info.keys()
while (1):
    name=str(input('Enter Name: '))
    if name in k:
        i=3
        while(i>0):
            pin=int(input('Enter PIN: '))
            if pin==info[name][2]:
                a=atm(name)
                while(1):
                    print('Enter 1 For Account Info')
                    print('Enter 2 For PIN Change')
                    print('Enter 3 For Balance Inquiry')
                    print('Enter 4 For Withdrawal')
                    print('Enter 5 For Deposit')
                    s=int(input('Select Operation: '))
                    if s==1:
                        a.acc_info()
                    elif s==2:
                        a.pin_change()
                    elif s==3:
                        a.acc_balance()
                    elif s==4:
                        a.withdraw()
                    elif s==5:
                        a.deposit()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter Y to exit, press any other key to continue operations: ')
                    if e=='y' or e=='Y':
                        print('Thank You!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
        break
        
