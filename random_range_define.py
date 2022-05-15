import random
x = input('please enter first number')
y = input('please enter the last number')
x=int(x)
y=int(y)

r=random.randint(x,y)
count = 0
while True:
	count += 1
	number = input('please guess a number')
	number = int(number)
	if number == r:
		print('correct!this is your', count,'times')
		break
	elif number > r:
		print('your guess is bigger than the number')
	else:
		print('your guess is smaller than the number')	
