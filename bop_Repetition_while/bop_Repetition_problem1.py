print('Start inputing numbers:')
number = int(input())
nofn = 0
numsum = 0
while number !=0:
    nofn += 1
    numsum += number
    number = int(input())
print('avarage:',numsum/nofn,'number of numbers' , nofn)