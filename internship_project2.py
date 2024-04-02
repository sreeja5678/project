input_text = input("Enter a sentence or paragraph: ")
# word_counter is used to count number of words in given input
def word_counter(text):
    """
    This function takes a string as input and returns the number of words in it.
    It splits the string by spaces and removes any empty elements from the list,
    then returns the length of the list, which is the word count.
    """
    words_list = text.split()
    words_list = [word for word in words_list if word]
    return len(words_list)
# This if-else is used to reduce errors
if not input_text:
    print("Error: Empty input. Please enter a sentence or paragraph.")
else:
    word_count = word_counter(input_text)
    print(f"Word count: {word_count}")