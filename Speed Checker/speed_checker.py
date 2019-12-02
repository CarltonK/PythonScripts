def check_speed(speed):
    speed_points = 0
    if speed.isdigit():
        speed = int(speed)
        if speed <= 70:
            print('OK')
        else:
            for i in range(70,speed,5):
                speed_points += 1     
                if speed_points > 12:
                    print('License suspended')
                    break

            print('Points \n ',speed_points)
                
    else:
        print('Enter a digit')

user_speed = input('Enter the Driver\'s speed:')
check_speed(user_speed)