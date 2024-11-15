# Reverse dictionary search; value -> key
def reverse_search_dict(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]

# Word count; string -> num words (num spaces + 1)
def word_counter(input):
    word_count = 1
    for i in input:
        if i == " ":
            word_count += 1
    return word_count