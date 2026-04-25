import os

# خيارات
Add = "1"
Sub = "2"
Mul = "3"
Div = "4"
Exit = "5"

# العمليات
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# القائمة 
def menu():
    os.system("cls")
    
    print("╔══════════════════════════════════════╗")
    print("║        Welcome to Calculator         ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Add                              ║")
    print("║  2. Subtract                         ║")
    print("║  3. Multiply                         ║")
    print("║  4. Divide                           ║")
    print("║  5. Exit                             ║")
    print("╚══════════════════════════════════════╝")
    
    return input("Enter your choice (1-5): ")

# إدخال الأرقام
def get_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1, num2

# البرنامج الرئيسي
while True:
    
    choice = menu()
    
    if choice == Exit:
        print("Good bye")
        break
    
    elif choice in [Add, Sub, Mul, Div]:
        num1, num2 = get_numbers()
        
        if choice == Add:
            print("Result:", add(num1, num2))
            
        elif choice == Sub:
            print("Result:", subtract(num1, num2))
            
        elif choice == Mul:
            print("Result:", multiply(num1, num2))
            
        elif choice == Div:
            print("Result:", divide(num1, num2))
        
        input("Press Enter to continue...")
    
    else:
        print("Invalid choice")
        input("Press Enter to continue...")