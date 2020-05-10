pi_file = open('/Users/paulinaignacak/Desktop/Python Learning/EDX/digits_of_pi.txt', 'r')

name = input('What is your name? ')
print('Hi',name)

seed = len(name)

pi_file.seek(seed)
digit = pi_file.read(1)

guess = input('Enter a single digit guess or "q" to quit: ')

correct = 0
wrong = 0

while guess.isdigit():
    if digit == '.':
        digit = pi_file.read(1)
    elif digit == '\n':
        seed += 1
        pi_file.seek(seed)
        digit = pi_file.read(1)
    else:
        if int(guess) == int(digit):
            print('Correct')
            correct += 1
        else:
            print('Incorrect')
            wrong += 1
    guess = input('Enter a single digit guess or "q" to quit: ')
    digit = pi_file.read(1)

print('Correct:',correct,'\n','Incorrect:',wrong)
pi_file.close()