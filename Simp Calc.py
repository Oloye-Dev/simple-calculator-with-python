#Simp Calc
print ('enter first num')
userInput1 = float(input())
print('enter arith, either + - / * %')
arith = input()
print ('enter the remaining num')
userInput2 = float(input())
while True:
    if arith == '+':
        result = (userInput1) + (userInput2)
        print(str(result))
        break
    elif arith == '-':
        result = (userInput1) - (userInput2)
        print(str(result))
        break
    elif arith == '*':
        result = (userInput1) * (userInput2)
        print(str(result))
        break
    elif arith == '/':
        if userInput2 == 0:
            print ('Error: Division by zero is not allowed.')
        else:
            result = (userInput1) / (userInput2)
            print(str(result))
        break
    elif arith == '%':
        result = (userInput1) % (userInput2)
        print(str(result))
        break
