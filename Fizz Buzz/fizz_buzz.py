def fizz_buzz(number):
	number = int(number)
	if number%3 == 0 and number%5 == 0:
		print('FizzBuzz')
	elif number%3 == 0:
		print('Fizz')
	elif number%5 == 0:
		print('Buzz')
	else:
		print('This number is not divisible by either 3 or 5')


user_value = input('Enter a number: ')
fizz_buzz(user_value)