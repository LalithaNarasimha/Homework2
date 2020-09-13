# Code that compute the squares and cubes for numbers from 0 to 5, 
# each cell occupies 20 spaces and right-aligned
numbers = [ 0, 1, 2, 3, 4, 5]
place_width = 20

header1 = 'Number'
header2 = 'Square'
header3 = 'Cube'

print('\nSolution 1\n')
print(f' {header1: >{place_width}} {header2: >{place_width}} {header3: >{place_width}}')
for num in numbers:
    print(f' {num: >{place_width}} {num ** 2: >{place_width}} {num**3: >{place_width}} ')

# Code that use this formula to calculate and print the Fahrenheit temperature 
celsius_value = [-40, 0, 40, 100]
f = 0

print('\nSolution 2\n')
for value in celsius_value:
    f = (9/5 * value) + 32
    print(f'Fahrenheit temperature for Celsius scale {value} is {f}')


# Code that input three integers from the user and print the sum and average of the numbers  

input_seq = [1000, 2000, 4000]
total = 0
seq = 0
average = 0

print('\nSolution 3\n')
for input in input_seq:
    total = total + input
    seq = seq + 1

average =  total/seq  
print(f'The sum {total:,d} ')
print(f'The average is {average:,.2f}')

  