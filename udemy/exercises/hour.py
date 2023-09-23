# Hour

hour = input('What time is now? ')

morning = 0
afternoon = 12
night = 18

try:
    int_hour = int(hour)
    if 0 <= int_hour <= 23:
        if morning <= int_hour < afternoon:
            print('Good morning!')
        elif afternoon <= int_hour < night:
            print('Good afternoon!')
        elif int_hour >= night:
            print('Good evening!')
    else:
        print('This is not a valid hour, the hour should is in 0 and 23!')
except:
    print('This is not a valid hour!')
