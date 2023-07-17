# Create a python script:
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.
# Commit script to git repository and provide link as home task result.

import random  # import random library to fill into list random values

my_list = [random.randint(0, 1000) for _ in range(100)]     # initialization of the new list and filling in by 100 random ins in range 0-1000

my_sorted_list = []     # initialization of the empty list to keep sorted list of ints
for x in range(len(my_list)):       # initialization of the loop to go threw the initial list
    min_value = my_list[0]          # initialization of the variable to keep min value and assign to first item of the list
    for y in range(len(my_list) - 1):   # initialization of the loop threw list of ints to find min value
        if my_list[y + 1] < min_value:  # check if current value is less than minimum stored value
            min_value = my_list[y + 1]  # assign found less value as a min
    my_sorted_list.append(min_value)    # add found min value to the new list
    my_list.remove(min_value)           # remove found min value from the initial list

average_even = 0        # initialize variable to keep average even numbers
average_odd = 0         # initialize variable to keep average odd numbers
even_counter = 0        # initialize variable to keep amount of even numbers
odd_counter = 0         # initialize variable to keep amount of odd numbers

for x in range(len(my_sorted_list)):        # loop threw the sorted list of ints
    if x % 2 == 0:         # if item number is odd
        average_odd += my_sorted_list[x]    # sum it up to the proper variable
        odd_counter += 1                    # increase counter amount
    else:                  # if item number is even
        average_even += my_sorted_list[x]   # sum it up to the proper variable
        even_counter += 1                   # increase counter amount

average_even /= even_counter      # divide sum to amount of numbers
average_odd /= odd_counter        # divide sum to amount of numbers

print('Average odd = ', average_odd)    # print result to the console
print('Average even = ', average_even)  # print result to the console


