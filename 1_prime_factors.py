# Write a function that finds the sum of all prime factors of a given number, n.

import math

def sum_of_prime_factors(a_number):
    # prime_factor_list = []
    sum_of_prime_factors = 0
    while a_number % 2 == 0:
        # prime_factor_list.append(2)
        sum_of_prime_factors = sum_of_prime_factors + 2
        a_number = a_number / 2
    
    for each_number in range(3,int(math.sqrt(a_number))+1,2):
      while (a_number % each_number == 0):
        # prime_factor_list.append(each_number)
        sum_of_prime_factors = sum_of_prime_factors + each_number
        a_number = a_number / each_number

    return sum_of_prime_factors


print(sum_of_prime_factors(650))