def fibonacci_generator(number):
    number = int(number)
    num1 = 0
    num2 = 1
    num_count = 1
    fib_list = [num2]
    
    while num_count < number:
        num_total = num1 + num2
        num1 = num2
        num2 = num_total
        num_count += 1
        fib_list.append(num_total)
        
    print(fib_list)