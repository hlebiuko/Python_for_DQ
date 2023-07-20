# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random
import string
from collections import defaultdict


def dict_sort(my_dict: dict) -> dict:       # function that gets dict as argument and return sorted dict                    # sorting list of keys from the dict
    return dict(sorted(my_dict.items()))


# Function that gets random amount of dicts and generate it
# While loop was selected to avoid possibility to miss duplicated values if the same letter will be generated and
# get provided amount of keys in the dict even if it was generated by random
def generating_of_dictionary_with_random_values() -> dict:
    this_dict = {}      # initialization of the empty dict
    keys_amount = random.randint(3, 26)         # initialization of random amount of pairs to generate
    while True:  # Loop for filling in the dict
        this_dict[random.choices(string.ascii_lowercase)[0]] = random.randint(0, 100)  # adding random char as
        # a key and random int in range 0-100 as a pair into the dict
        if len(this_dict) == keys_amount:  # Check if required amount of keys are already generated
            break  # Closing the loop filling the dict
    print(this_dict)
    return dict_sort(this_dict)     # return created dict


# Function to generate list of dicts, gets int value as amount of dicts to append, as default gets random value
def generating_list_of_dicts_with_random_values(number_of_dicts_in_list=random.randint(3, 10)) -> list:
    list_of_dicts = []  # initialization of variable to collect generated dictionaries
    for x in range(number_of_dicts_in_list):
        list_of_dicts.append(generating_of_dictionary_with_random_values())
    return list_of_dicts        # return generated list of dicts


# Using defaultdict to get dict with all the keys and list of all value for this key
# It was used to find elements, that has the greatest values at first appearance for not to lose the data
def get_dict_will_all_values_from_list_of_dict(list_of_dicts: list) -> defaultdict:
    dict_with_all_values = defaultdict(list)
    for sub_dict in list_of_dicts:  # Iterate threw the list of dicts
        for key in sub_dict:  # Iterate threw the keys of iterated dict
            dict_with_all_values[key].append(sub_dict[key])  # append value of the key to existed or created key
    return dict_with_all_values


# Task 2 part 2
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.

# Function to compress list of dicts to one common dict
def compressing_list_of_dicts_to_one_dict(list_of_dicts: list) -> dict:
    temp_common_dict = {}       # initialization of the temp dict
    final_dict = {}             # initialization variable for dict that will be returned
    dict_for_keys_with_duplicates = {}      # initialization of the dict to keep keys with duplicates in different dicts
    number_of_dict = 0          # variable to hold number of the dict to fill pair key:value
    dict_with_all_values = get_dict_will_all_values_from_list_of_dict(list_of_dicts)
    for observed_dict in list_of_dicts:     # loop to go threw list of dicts
        for observed_key in observed_dict:  # loop to go threw keys in dict
            if observed_key in temp_common_dict:    # check if selected key is already present in other dicts
                if observed_dict[observed_key] > temp_common_dict[observed_key]:    # if already present value for
                    # this key is less that current one
                    temp_common_dict[observed_key] = observed_dict[observed_key]    # then add value to temp dict
                    dict_for_keys_with_duplicates[observed_key] = number_of_dict    # and save number of the dict
            else:                                                                   # else
                temp_common_dict[observed_key] = observed_dict[observed_key]        # add pair to temp dict
                if len(dict_with_all_values[observed_key]) != 1:                    # if key is present more that once
                    dict_for_keys_with_duplicates[observed_key] = number_of_dict    # save number of the dict
        number_of_dict += 1                                                         # increase counter of the dicts

    keys_of_temp_dict = list(temp_common_dict.keys())                              # getting list of keys from temp dict
    for x in range(len(temp_common_dict)):             # loop to go threw temp dict
        if keys_of_temp_dict[x] in dict_for_keys_with_duplicates:   # if key is present in several dicts
            # add pair to final dict with changed key and max value
            final_dict[str(keys_of_temp_dict[x]) + "_" + str(dict_for_keys_with_duplicates[keys_of_temp_dict[x]])] = temp_common_dict[keys_of_temp_dict[x]]
        else:       # else
            final_dict[keys_of_temp_dict[x]] = temp_common_dict[keys_of_temp_dict[x]]   # add pair to final dict

    return dict_sort(final_dict)        # return sorted final dict


print(compressing_list_of_dicts_to_one_dict(generating_list_of_dicts_with_random_values()))


