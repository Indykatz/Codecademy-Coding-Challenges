# You have a bag containing tiles with numbers [1, 2, 3, …, 100] written on them. Each number appears exactly once, so there are 100 tiles and 100 numbers. Now, without looking, one number tile is randomly picked out of the bag and discarded. Write a function, missingNo, that will find the missing number


import random

def missingNo(input_list):
    full_list = list(range(1,101))
    for index in range(1, 101, 1):
        if full_list[index] != input_list[index]:
            return full_list[index]


def missingList():
    missing_list = list(range(1,101))
    random_number = random.randint(1,101)
    missing_list.remove(random_number)
    return missing_list


print(missingNo(missingList()))