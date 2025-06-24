#It takes a filepath as input and returns the contents of the file as a string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    text = (get_book_text(path_to_file))
    num_words = len(text.split()) 
    return num_words

#function that takes the text from the book as a string, 
# and returns the number of times each character appears in the string

def get_char_counts(path_to_file):
    text = (get_book_text(path_to_file))
    lower_case = str.lower(text)
    char_counts = {}

    for letter in lower_case:
        if letter in char_counts:
            char_counts[letter] +=1
        else:
            char_counts[letter] = 1
    return char_counts
            

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries


def sort_on(items):
    return items["num"]

def sort_dictionary(char_counts):  # Accept the dictionary as an argument
    char_list = []
    for char, num in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list  # Instead of printing, let the caller decide what to do!

