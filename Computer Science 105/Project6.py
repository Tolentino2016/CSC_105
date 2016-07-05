
def lineNumbers(filename):
    

    infile = open(filename, 'r')
    count = 0

    for line in infile:
        count += 1
        print (count ,':'line)

    infile.close()

main()

# Exercise 5, chapter 6

def sumNumbers(filename):

def main():

    total = 0.0
    infile = open('numbers.txt','r')

    for line in infile:
        amount = float(line)
        total += amount

    infile.close()

    print(format(total,'.2f))

main()

# Exercise 5, chapter 7
def chargeAccountValidation(filename, test_account):
    
def main():

    total = 0.0
    infile = open('numbers.txt', 'r')

    for line in infile:
        amount = float(line)
        toatal += amount

    infile.close()

    print(format(total, '2f))


# Exercise 7, chapter 7
def driversLicenseExam(filename):
    
incorr_count = 0
num_questions = 20
incorr_list = []

infile = open('user_answer.txt','r')

user_ans_list = infile.readlines()

infile.close()

index = 0

while index < 20:
    if user_ans_list[index].rstrip('\n') == corr_ans_list[index]:
        corr_count += 1
        index += 1
    else:
        incorr_count =+ 1
        index += 1
        incorr_list.append(index)

    if corr_count >= 15:
        print('You  passes the exam')
    esle:
        print('You did not pass the exam')

    print('Total Correct: ', corr_count)
    print('Total Incorrect: ', incorr_count)
    print('List of Incorrect answers: ', incorr_list)

main()

