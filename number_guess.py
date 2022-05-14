i=3
pwd = 'a123456'

while True:
	i=i-1
	k = input('please guess a number') 
	if k == pwd:
		print('you are correct!')
		break
	else:
		if i == 0:
			break
		else:
			print('Wrong!you still have',i,'times') 	
		
