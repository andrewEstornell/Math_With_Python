# Consider the first N digits of pi. For each N, let c3(N) be the length of the longest run of threes in those N digits.
# Compute c3(N) for enough values of N to form a hypocrisies.
import numpy as np

# Parameters for 10 billion testing
file_size = 10 ** 10
file_name = 'pi-10-billion.txt'

# Parameters for 1 million testing
#file_size = 10 ** 6
#file_name = 'pi-1-million.txt'


fp = open(file_name)

digit_block = 10 ** 4
# Stores the current number of adjacent 3s
threes = 0
max_threes = 0
# Reads the digits in chunks of a given size
string_pi = fp.read(digit_block)
i = 0
while string_pi:
    # Iterates through all digits in the selected chunk and checks for adjacent 3s
    for j in range(digit_block):
        if string_pi[j] == '3':
            threes += 1
            if threes > max_threes:
                max_threes = threes
                print('Max 3s = ', max_threes, '   N = ', i + j)
        else:
            threes = 0
    i += digit_block
    string_pi = fp.read(digit_block)

print('END: ')
print('Max 3s = ', max_threes, '   N = ', i)

# Displays the frequency of digits
fp = open(file_name)

string_pi = fp.read(digit_block)
i = 0
digits = np.zeros(10)
while i < file_size:
    for j in range(digit_block):
        if string_pi[j] == '\n':
            continue
        digits[int(string_pi[j])] += 1
    i += digit_block
    string_pi = fp.read(digit_block)
for j in range(10):
    print(j, digits[j] / i)
