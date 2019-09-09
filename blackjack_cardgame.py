def black_jack(numbers):
    for num in numbers:
        if num in range(1,12):
            if sum(numbers) <= 21:
                return sum(numbers)
            elif sum(numbers) > 21 and 11 in numbers:
                return (sum(numbers) - 10)
            else:
                return 'BUST'
            
            
num_list = []
count = 3
while count >= 1:
    num_count = input('Enter a number: ')
    num_count = int(num_count)
    num_list.append(num_count)
    count -= 1
    
black_jack(num_list)