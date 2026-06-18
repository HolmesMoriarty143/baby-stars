#Arithmetic Calculator
print("\tWelcome to Basic Arithmetic Calculator")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
while True:
    choice=int(input("Choose Your Desired Operation:- \n\t1.Addition\n\t2.Subtraction\n\t3.Multiplication\n\t4.Division\n\t5.Modulus\n\t6.Floor Division\n\t7.Exponentiation\n\t8.End\nEnter your Choice: "))
    if choice == 1:
        print("Addition: The sum of ",n1," and ",n2," is ",n1+n2)
    elif choice == 2:
        print("Subtraction: The difference of ",n1,"and",n2," is ",n1-n2)
    elif choice == 3:
        print("Multiplication: The Product of ",n1," and ",n2," is ",n1*n2)
    elif choice == 4:
        print("Division: The Quotient of ",n1," and ",n2," is ",n1/n2)
    elif choice == 5:
        print("Modulus: The Remainder of ",n1," and ",n2," is ",n1%n2)
    elif choice == 6:
        print("Floor Division: The Floor Division of ",n1," and ",n2," is ",n1//n2)
    elif choice == 7:
        print("Exponentiation : The Exponent of ",n1," and ",n2," is ",n1**n2)
    elif choice == 8:
        print("\tThank You")
        break
else:
    print("Invaild Choice")
#End of Program
