#Aniket Prajapati
#SYCS
#351
def fact(number):
   
    fact = 1
  
    for number in range(number, 1,-1):
    
        fact = fact * number
    return fact

number = int(input("Enter The Number : "))

factorial = fact(number)
print("Factorial is "+str(factorial))
