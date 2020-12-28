from Functions import Funcs_time

print('Welcome to the time converter, please indicate which element you would like to convert according to the number.')

while True:
    print('[1] Seconds\n'
          '[2] Minutes\n'
          '[3] Hours\n'
          '[4] Days\n'
          '[5] Weeks\n'
          '[0] Quit')
    start = int(input('Convert from: '))
    if start == 1:
        end = int(input('To: '))
        qty = float(input('Seconds: '))
        if end == 1:
            print(f'{qty} seconds is {qty} seconds.')
        elif end == 2:
            result = Funcs_time.sec_to_min(qty)
            print(f'{qty} seconds is {result} minutes.')
        elif end == 3:
            result = Funcs_time.sec_to_hour(qty)
            print(f'{qty} seconds is {result} hours.')
        elif end == 4:
            result = Funcs_time.sec_to_day(qty)
            print(f'{qty} seconds is {result} days.')
        elif end == 5:
            result = Funcs_time.sec_to_week(qty)
            print(f'{qty} seconds is {result} weeks.')
        elif end == 0:
            print(f'You have chosen to quit, thank you.')
            break
    elif start == 2:
        end = int(input('To: '))
        qty = float(input('Minutes: '))
        if end == 1:
            result = Funcs_time.min_to_sec(qty)
            print(f'{qty} minutes is {result} seconds.')
        elif end == 2:
            print(f'{qty} minutes is {qty} minutes.')
        elif end == 3:
            result = Funcs_time.min_to_hour(qty)
            print(f'{qty} minutes is {result} hours.')
        elif end == 4:
            result = Funcs_time.min_to_day(qty)
            print(f'{qty} minutes is {result} days.')
        elif end == 5:
            result = Funcs_time.min_to_week(qty)
            print(f'{qty} minutes is {result} weeks.')
        elif end == 0:
            print(f'You have chosen to quit, thank you.')
            break
    elif start == 3:
        end = int(input('To: '))
        qty = float(input('Hours: '))
        if end == 1:
            result = Funcs_time.hour_to_sec(qty)
            print(f'{qty} hours is {result} seconds.')
        elif end == 2:
            result = Funcs_time.hour_to_min(qty)
            print(f'{qty} hours is {result} minutes.')
        elif end == 3:
            print(f'{qty} hours is {qty} hours.')
        elif end == 4:
            result = Funcs_time.hour_to_day(qty)
            print(f'{qty} hours is {result} days.')
        elif end == 5:
            result = Funcs_time.hour_to_week(qty)
            print(f'{qty} hours is {result} weeks.')
        elif end == 0:
            print(f'You have chosen to quit, thank you.')
            break
    elif start == 4:
        end = int(input('To: '))
        qty = float(input('Days: '))
        if end == 1:
            result = Funcs_time.day_to_sec(qty)
            print(f'{qty} days is {result} seconds.')
        elif end == 2:
            result = Funcs_time.day_to_min(qty)
            print(f'{qty} days is {result} minutes.')
        elif end == 3:
            result = Funcs_time.day_to_hour(qty)
            print(f'{qty} days is {result} hours.')
        elif end == 4:
            print(f'{qty} days is {qty} days.')
        elif end == 5:
            result = Funcs_time.day_to_week(qty)
            print(f'{qty} days is {result} weeks.')
        elif end == 0:
            print(f'You have chosen to quit, thank you.')
            break
    elif start == 5:
        end = int(input('To: '))
        qty = float(input('Weeks: '))
        if end == 1:
            result = Funcs_time.week_to_sec(qty)
            print(f'{qty} weeks is {result} seconds.')
        elif end == 2:
            result = Funcs_time.week_to_min(qty)
            print(f'{qty} weeks is {result} minutes.')
        elif end == 3:
            result = Funcs_time.week_to_hour(qty)
            print(f'{qty} weeks is {result} hours.')
        elif end == 4:
            result = Funcs_time.week_to_day(qty)
            print(f'{qty} weeks is {result} days.')
        elif end == 5:
            print(f'{qty} weeks is {qty} weeks.')
        elif end == 0:
            print(f'You have chosen to quit, thank you.')
            break
    elif start == 0:
        break