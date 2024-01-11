# sum of two inputed digit number

a = input("enter two digit number ")

#changing a from integer to string 
a = str(a)

#seprating 2 digits
b = a[0]
c = a[1]

# taking sum by changing 2 seperated digits from string to intetger 
sum = int(b) + int (c)

print(sum)
