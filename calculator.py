print('Simple calculator')
# Function
def add(x,y):
    return (x+y)
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return 'error'
    return x//y
# User input

num1=int(input('Enter your 1st num:',))
num2=int(input('Enter your 2st num:'))
print('1.ADD')
print('2.SUB')
print('3.MUL')
print('4.DIV')
option=int(input('Enter 1/2/3/4:'))

if option==1:
    print(f'Result:{add(num1,num2)}')
elif option==2:
    print(f'Result:{sub(num1,num2)}')
elif option==3:
    print(f'Result:{mul(num1,num2)}') 
elif option==4:
    print(f'Result:{div(num1,num2)}')       

