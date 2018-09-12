def factorial(x) :
  if x==1 :
    return 1
  return x*factorial(x-1)
print ("Hello User")
y = int(input("Enter the number whose factorial is to be calculated : "))
print('The required answer is :' , factorial(y)
