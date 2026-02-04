num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# print("Result",calculator())
def calculate(a, b, op):
    calDict={
        "+": a+b,
        "-": a-b,
        "*": a*b,
        "/": "Number 2 can't be 0 for division" if b==0 else a/b
    }
    return calDict.get(op, 'Please select valid operation')

result = calculate(num1, num2, operation)
print("Result:: ",result)
