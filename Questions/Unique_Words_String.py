'''Write a program in Python that takes a string as input and returns the count of unique words in the string. Consider a word to be any sequence of characters separated by spaces or punctuation marks. Ignore case sensitivity when counting unique words.
Example: Input: "The cat and the Hat!"
Output: 4
Note: The program should treat "The" and "the" as the same word.
'''
def unique_words(input_str):
    input_str=input_str.lower()
    words_list=input_str.split()
    words_set=set(words_list)
    return len(words_set)

input_str=str(input("Enter a string: "))
print(unique_words(input_str))
