###                 TASK 9
##Ask 2 numbers from users and store it in num1 and num2
##Ask user to press 1 for addition,2 for subtraction,3 for multiplication and 4 for division
##based on number given by user do the math operation

print ("1. ADD")
print ("2. SUBTRACT")
print ("3. DIVIDE")
print ("4. MULTIPLY")

operation = input()
if operation == "1":
    A = input("Enter the first number: ")
    B = input ("Enter the second number: ")
    print("SUM =" + str(int(A)+int(B)))
elif operation == "2":
    A = input("Enter the first number: ")
    B = input ("Enter the second number: ")
    print("DIFFERENCE =" + str(int(A)-int(B)))
elif operation == "3":
    A = input("Enter the first number: ")
    B = input ("Enter the second number: ")
    print("RESULT =" + str(int(A)/int(B)))
elif operation == "4":
    A = input("Enter the first number: ")
    B = input ("Enter the second number: ")
    print("PRODUCT =" + str(int(A)*int(B)))
else:
    print ("INVALID ENTRY")
