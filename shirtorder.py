sizes = ('S, M, L')

small = 0
medium = 0
large = 0
shirts_total = 0


while True:
	shirt_size = input('Do you want a shirt S, M, or L? Type exit when you are done: ').lower()
	if shirt_size.startswith('e'):
		print()
		break
	elif shirt_size == 's':
		small += 1
	elif shirt_size == 'm':
		medium += 1
	elif shirt_size == 'l':
		large += 1
	else:
		print ('invalid entry')

	shirts_total += 1
	s_cost = small * 6
	m_cost = medium * 7
	l_cost = large * 8
	cost_total = s_cost + m_cost + l_cost

print('You are buying',shirts_total,'shirts total.')
print('You have:','\t',small,'small shirts','\t',medium,'medium shirts','\t',large,'large shirts')
print ('It will cost you $',cost_total)
