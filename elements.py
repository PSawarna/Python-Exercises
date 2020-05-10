elements_file = open('/Users/paulinaignacak/Desktop/Python Learning/EDX/elements1_20.txt', 'r')
elements = elements_file.readline()

elements_list = []

while elements:
    elements_list.append(elements.strip('\n').lower())
    elements = elements_file.readline()

def get_names():
    element_names = []
    for guess in range(5):
        guess = input('list any 5 of the first 20 elements in the Period table: ')
        if guess in element_names:
            print('You cannot enter an element twice.')
        elif guess == '':
            pass
        else:
            element_names.append(guess)
    return element_names

names = get_names()
total = 0
found = []
not_found = []

for item in names:
    if item in elements_list:
        found.append(item)
        total += 1
    else:
        not_found.append(item)

print(total*20,'% correct')
print('Elements found:',found)
print('Elements not found:',not_found)