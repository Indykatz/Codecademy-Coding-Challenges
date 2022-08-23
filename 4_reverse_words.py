# Write a function that will take a given string and reverse the order of the words. “Hello world” becomes “world Hello” and “May the Fourth be with you” becomes “you with be Fourth the May”

def reverse_words(a_string):
    reversed_string = a_string.split()
    reversed_string.reverse()
    return ' '. join(reversed_string)

print(reverse_words("Hello world"))
print(reverse_words("May the Fourth be with you"))