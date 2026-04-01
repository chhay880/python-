# NUM1=30
# NUM2=4
# NUM3=5
# NUM4=90
# NUM5=6
# NUM6=2
# PRINT=(NUM5*NUM4)*(NUM6**NUM4)


# num=int(input("enter the no:"))
# for i in range(1, 11):
#     print( num, "*", i, "=",num * i)

# num=int(input("enter the no:"))
# num1=int(input("enter the no:"))
# for i in range(num,num1):
#     if i % 2==0:
#         print(i)
#     if i % 4==0:
#      print("yes")
#     else:
#      print("No")   

# num=int(input("enter the no:"))
# if(num % 7==0):
#     print("true")
# else:
#     print("false")

# num=int(input("enter the no:"))
# num1=int(input("enter the no:"))
# sum=0
# for i in range(num,num1):
#     sum=sum+i
# print(sum)

# num=str(input("enter the word:"))
# if("num==a,e,i,o,u"):
#     print("yes")
# else:
#     print("no")

# num=input("enter the words:")
# vowels= "aeiouAEIOU"
# found = False
# for i in vowels:
#     found=True
# if found:
#     print("yes")
# else:
#     print("No")

# str=input("enter the words:")
# vowels= "aeiouAEIOU"
# for i in str:
#     if i in vowels:
#         check=True
# if(check):
#     print("yes")
# else:
#         print("no")


num=int(input("enter the no:"))
remi=0
reverse=0
sum=0
while(num>0):
    remi=num % 10
    print("reminder: ",remi)
    sum = sum+remi
    num//=10
    reverse=reverse*10+remi
print(reverse)
print("sum of remainders:", sum)
# num=reverse
# print(num)