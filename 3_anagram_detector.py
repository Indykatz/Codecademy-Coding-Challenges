# Write a function in your favorite programming language that will accept any two strings as parameters and return “1” if they are anagrams and “0” if they are not.

def anagram_dector(word_1, word_2):
    return_value = 0
    if sorted(word_1.lower()) == sorted(word_2.lower()):
        return_value = 1
    return return_value
 

print(anagram_dector("Silent", "Listen"))
print(anagram_dector("Hello", "Wolrd"))