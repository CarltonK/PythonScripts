def binary_password_checker(password):
    # Maintain a count of total points
    binary_points = 0
    
    # List of upper case characters
    characters_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # Keep count of upper case characters
    upper_list = []
    
    # List of lower case characters
    characters_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Keep count of lower case characters
    lower_list = []
    
    # List of numbers
    characters_numbers = ['0','1','2','3','4','5','6','7','8','9']
    # Keep count of number characters
    number_list = []
    
    # List of special characters
    characters_special = ['!','@','#','$','%','^','&','*','-','_','=','+','\'','?','\"','/','<','>','.',',']
    # Keep count of special characters
    special_list = []
        
    if len(password) >= 8:
        binary_points += 1
    if len(password) < 8:
        binary_points -= 1
        print('Please consider making your password 8 characters or more')
        
    
    for character in password: 
        if character in characters_upper:
            binary_points += 1
            upper_list.append(character)
        elif character in characters_lower:
            binary_points += 1
            lower_list.append(character)
        elif character in characters_numbers:
            binary_points += 1
            number_list.append(character)
        elif character in characters_special:
            binary_points += 1
            special_list.append(character)
        else:
            binary_points -= 1
            
    if len(upper_list) == 0:
        print('Please consider adding atleast ONE upper case character')
    if len(lower_list) == 0:
        print('Please consider adding atleast ONE lower case character')
    if len(number_list) == 0:
        print('Please consider adding atleast ONE number character')
    if len(special_list) == 0:
        print('Please consider adding atleast ONE special character')
        
    return binary_points

def binary_points_checker():
    password = input('Enter your password: ')
    points = binary_password_checker(password)
    
    
    print('.....RESULTS.....')
    # Grading System
    if points in range(0,9):
        print('Your password is weak')
    elif points in range(9,13):
        print('Your password is fairly strong')
    elif points in range(13,18):
        print('Your password is strong')
    elif points in range(18,100):
        print('Your password is very strong')
        
binary_points_checker()