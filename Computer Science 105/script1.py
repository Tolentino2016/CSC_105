#script 1 

x = int(input('Enter a nonnegative integer:'))
count = 1
y = 1
while count <= x:
    y = count * y
    count = count+ 1
print(y)
