#Калькулятор:
#Це класичний початковий проєкт.
#Напиши просту програму, яка приймає два числа від користувача і виконує базові операції 
# (додавання, віднімання, множення, ділення).

number1 = float(input("введіть число від 1 до 100\n"))
number2 = float(input("введіть число від 1 до 100\n"))
operation = input("виберіть одну математичну дію (+,-,/,*)\n")


def calculate (num1,num2):
    if operation == "+":
        return num1+num2
    elif operation== "-":
        return num1-num2
    elif operation =="/" and num2==0 :
        return "На 0 ділити не можна"
    elif operation == "/":
        return num1/num2
    elif operation == "*":
        return num1*num2
    else:
        return "Перевірте свій вираз.Невірно введений символ "

print(calculate(number1,number2))  