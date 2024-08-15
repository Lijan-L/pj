print('______ATM_______')
PIN=int(input('enter your pin'))
if PIN==1234:
    myamount=10000
    print('1.withdraw money')
    print('2.check money')
    print('3.deposit')
    option=int(input('enter your option'))
    if option==1:
        Amount=int(input('the amount you want to wihdraw'))
        if Amount>myamount:
            print('low balance')
        else:
            newblc=myamount-Amount
            print('withdrawn amount',Amount)
            print('remaing blc',newblc)
    elif option==2:
       print('your balace is',myamount)
    elif option==3:
        Amount=int(input('enter a amount you want to deposit'))
        new=Amount+myamount
        print('total money',new)   
    else:
        print('invalid')   
  
        
    
else:
    print('wrong pin')


# print('______ATM_______')
# PIN = int(input('enter your pin: '))

# if PIN == 1234:
#     myamount = 10000
#     print('1. withdraw money')
#     print('2. check money')
#     option = int(input('enter your option: '))
    
#     if option == 1:
#         Amount = int(input('the amount you want to withdraw: '))
#         if Amount > myamount:
#             print('low balance')
#         else:
#             newblc = myamount - Amount
#             print('withdrawn amount:', Amount)
#             print('remaining balance:', newblc)
    
#     elif option == 2:
#         print('your balance is', myamount)
    
#     else:
#         print('invalid option')
        
# else:
#     print('wrong pin')