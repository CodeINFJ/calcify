num1 = float(input("enter first value: "))
num2 = float(input("enter first value: "))
operator= input("enter the operator{+,-,*,/}: ")


if (operator == "+"):
    sum = num1 + num2
    print(f'{num1} + {num2}= {sum}')

elif (operator == "-"):
    sub = num1 - num2
    print(f'{num1} - {num2}= {sub}')

elif (operator == "*"):
    mul = num1 * num2
    print(f'{num1} * {num2}= {mul}')

elif (operator == "/"):
    if (num2 == 0):
        print("sorry, a number is not divisible by zero")
    else:
        div = num1 / num2
        print(f'{num1} / {num2}= {div}')          

else:
    print("you have entered an invalid operatir")



