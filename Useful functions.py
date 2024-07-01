# Reverse dictionary search; value -> key
def reverse_search_dict(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]