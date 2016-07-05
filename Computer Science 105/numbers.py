##filein = open('myfile.txt')
##line1= filein.readline()
##number1 = int(line1)
##line2= filein.readline()
##number2 = int(line2)
##result = number1 + number2
##print('The sum of the numbers in the file is',result)
##filein.close()

filein = open('numbers.txt')
total = 0
for line in filein:
    number = int(line)
    total += number
print(' The sum of the numbers in the file', total)
filein.close()
