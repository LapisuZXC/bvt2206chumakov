print('Start inputuing strings:')
string = input()
vowel = 0
while string != '':
    vowel += string.count('a') + string.count('e') + string.count('i') + string.count('i')+ string.count('u')
    string = input()
print(vowel)
