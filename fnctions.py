#abs function
#steps = -3
#if abs(steps) > 0:
#	print('Character is moving')

steps = -3
if steps < 0 or steps > 0:
	print('character is moving')
	
#bool funvtion
print(bool(0))
print(bool(-40))

print(bool('ken'))
print(bool(None))

year = input('Enter Year of birth: ')
#if not bool(year.rstrip()):
if year == '':
	print("Error, you need to enter a year of birth")
	year = 2000
	print('we have given you a default year of birth')
	print(year)
	
	
dir(['a', 'short', 'list'])

eval("print('wow')")
eval('10*5')
