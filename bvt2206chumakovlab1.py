import math
a=[]
print('Введите кол-во уравнений:')
n0 = int(input())
n=3*n0

print('Введите коэффиценты уравнений')

for i in range(n):
    l=int(input())
    a.append(l)
for e in range(n0):
    k=3*(e+1)-1
    b = a[k-2:k+1]

    if (b[1])**2 - 4 * (b[0]) * (b[2]) < 0:
        print(' ')
        print("Ошибка: Дисккрименант меньше нуля")
    elif (b[1])**2 - 4 * (b[0]) * (b[2]) == 0:
        root = (-b[1])/ (2 * b[0])
        print(' ')
        print("Единстевенный корень уровнения №", e+1,':',root)
    else:
        print(' ')

        root1 = (-b[1] + math.sqrt((b[1])**2 - 4 * (b[0]) * (b[2]))) / (2 * b[0])
        print('Первый корень уравнения №',e+1,':',root1)

        root2 = (-b[1] - math.sqrt((b[1]) ** 2 - 4 * (b[0]) * (b[2]))) / (2 * b[0])
        print('Второй корень уравнения №', e+1, ':',root2)
