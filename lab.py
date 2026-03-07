#!/usr/bin/env python3

upper_number = int(input('How many items should we process with teh FizzBuzz logic?\n'))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')

    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)