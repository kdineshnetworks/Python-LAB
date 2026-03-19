s="abc"
s+= str(10) #This will concatenate the string "abc" with the string representation of the integer 10, resulting in "abc10".
print(s)

x="abc "
x*=5     #This will cause an error because you cannot multiply a string by a float. You can only multiply a string by an integer.
print(x)
