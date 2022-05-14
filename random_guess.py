import random
r = random.randint(1,100)

while True:
	x = input('please guess a integer in 1-100')
	x = int(x)
	if x == r:
		print('congratulation! it\'s correct!')
		break
	elif x > r:
		print('your guess is bigger than the number')
	else:
		print('your guess is smaller than the number')