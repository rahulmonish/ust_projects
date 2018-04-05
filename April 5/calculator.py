def factorial1():
    num= int(input("enter the number"))
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


def lcm():
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return greater


def factor(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)



ch="y"
while ch=="y" or ch=="Y":
    choice= input(print("Enter the option: \n 1. Factorial \n 2. LCM \n 3. HCM \n 4. Factor"))
    if choice=="1":
        factorial1()
    elif choice=="2":
        x = int(input("enter the first number"))
        y = int(input("enter the second number"))
        greater=lcm()
        print("LCM is : ", greater)
    elif choice=="3":
        x = int(input("enter the first number"))
        y = int(input("enter the second number"))
        greater = lcm()
        print("HCM is : ", int(x*y/greater))
    elif choice=="4":
        x = int(input("enter the number"))
        factor(x)
    ch= input("Do you want to continue y/n ?")

