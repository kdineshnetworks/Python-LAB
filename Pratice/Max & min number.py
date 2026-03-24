n=5
i=0
max= float('-inf') #negative infinity
min=float('inf') #positive infinity
print ("input", n , "n times")
while i<n:
    i=i+1
    x=int(input("Enter a number: "))
    if x>max:
        max=x
    if x<min:
        min=x
print ("Minimum number is:",min)
print("Maximum number is:",max) 
   
