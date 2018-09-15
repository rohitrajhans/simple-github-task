#this function returns the value of the factorial of the entered integer.
#Note - If a negative integer is entered, the return value is a string type.
def factorial(x) :
  if x == 0 :
    return 1  
  return x*factorial(x-1)
print ("Hello User")
factorial_of = int(input("Enter the number whose factorial is to be calculated : "))
while factorial_of < 0:
    print("The factorial of " + str(factorial_of) + " is not defined! Factorials are only defined for positive numbers. Let's try again!\n")
    factorial_of = int(input("Enter the number whose factorial is to be calculated : "))
print('The required answer is :' , factorial(y)
