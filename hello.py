print('hello, world')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
L[0][0] = 'zzz'
print(L[0][0])

age = input('age: ')
if age < 18:
	print('teen')
elif age == 18:
	print('ready for adult')
else :
	print('adult')

arr = [1, 3, 4, 45, 56, 57, 200]
for x in arr:
	if x > 100:
		print('Found')
		break