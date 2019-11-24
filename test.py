repeat = 'y'

while repeat == 'y':
    repeat = input('Do you want to run another api call? [y/n]: ')
    while repeat != 'y' and repeat != 'n':
        print('can only enter y or n')
        repeat = input('Do you want to run another api call? [y/n]: ')

