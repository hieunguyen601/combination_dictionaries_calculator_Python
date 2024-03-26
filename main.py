#calculator
#add
def add(n1,n2):
    return n1 + n2
#subtract
def subtract(n1,n2):
    return n1 - n2
#multiply
def multiply(n1,n2):
    return n1 * n2
#division
def division(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/": division,
}
num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")