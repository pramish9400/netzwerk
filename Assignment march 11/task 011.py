###                                 TASK 11
##Ask 2 numbers from users and store it in num1 and num2
##Ask user to press 1 for addition,2 for subtraction,3 for multiplication and 4 for division
##based on number given by user do the math operation



num1=int(input("input the number one: "))
num2=int(input("input the number one :"))
def add_num(a,b):
    sum=a+b;
    return sum; 

def sub_num(a,b):
    sum=a-b;
    return sum; 

def div_num(a,b):
    sum=a/b;
    return sum; 

def prod_num(a,b):
    sum=a*b;
    return sum; 

print ("1. ADD")
print ("2. SUBTRACT")
print ("3. DIVIDE")
print ("4. MULTIPLY")

operation = input()
if operation == "1":
    print("The sum is",add_num(num1,num2))
elif operation == "2":
    print("The difference is",sub_num(num1,num2))
elif operation == "3":
   print("The result is",div_num(num1,num2))
elif operation == "4":
   print("The product is",prod_num(num1,num2))
else:
    print ("INVALID ENTRY")

