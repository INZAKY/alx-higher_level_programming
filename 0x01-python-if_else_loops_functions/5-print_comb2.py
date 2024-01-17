#!/usr/bin/python3

# Print numbers from 0 to 99 with leading zeros and comma separation
formatted_numbers = ', '.join('{:02d}'.format(num) for num in range(100))
print(formatted_numbers)
