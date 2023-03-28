print('Start inputing numbers:')
number = int(input())
count = 0
while number != 0:
    if number % 7 == 0:
        count+=1
    number = int(input())
print(count)
