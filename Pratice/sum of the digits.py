n=int(input("Enter a number: "))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10 #integer division
print("Sum of the digits:",sum)
