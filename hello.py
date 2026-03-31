# num1=int(input("enter your no.:"))
# num2=int(input("enter your no.:    "))
# num3=int(input("enter your no.:"))
# if(num1>num2 and num1>num3):
#     print("num1 is greater")  
# elif(num2>num1 and num2>num3):
#     print("num2 is greater")
# else:
#     print("num3 is greater")

# import calendar               
# year=int(input("enter the year:"))
# if(calendar. isleap(year)):
#     print("leap year")  
# else:
#     print("non-leap year")

# S1=int(input("enter the marks:"))    
# H1=int(input("enter the marks:"))
# M1=int(input("enter the marks:"))
# E1=int(input("enter the marks:"))
# S2=int(input("enter the marks:"))
# result=(S1+H1+M1+E1+S2)
# result1=(result*100)
# result2=(result1/500) 
# print(result)
# print(result1)
# print(result2)
# if(result2<100) and (result2>=80):
#     print("Grade A")
# elif(result2<80) and (result2>=60):
#     print("Grade B")
# elif(result2<60) and (result2>=40):
#     print("Grade C")
# else:
#     print("Grade Fail")          
count=1
for rows in range(0,3):
    for column in range(0,3):
        print(count,end=" ")
        count +=1    
    print()  

count=0
for rows in range(0,3):
    for column in range(0,3):
        print(count,end=" ")
    print() 

count=9
for rows in range(0,3):
    for column in range(0,3):
        print(count,end=" ")
        count -=1    
    print() 