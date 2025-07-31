#write a code to add two numbers
def add_numbers(num1, num2):
    return num1 + num2
main = __name__ == "__main__"
if main:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    result = add_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {result}.")



