# Write a function, timesTables, that prints out multiplication tables (the type you learned in primary / grade school) up to 12x12.

def timesTables():
    for each_number in range (1, 13, 1):
        result = []
        for each_multiple in range(1, 13, 1):
            result.append(each_number * each_multiple)
        print(result)



timesTables()