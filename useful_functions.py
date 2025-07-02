import typing
def reverse_search_dict(dictionary: dict, value: any) -> any:
    """
    Reverse dictionary search; value -> key
    """
    return list(dictionary.keys())[list(dictionary.values()).index(value)]

def word_counter(input: str) -> int:
    """
    Word count; string -> num words (num spaces + 1)
    """
    word_count = 1
    for i in input:
        if i == " ":
            word_count += 1
    return word_count

def mergesort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.
    """
    if len(lst) == 1:
        return lst[:]
    else:
        middle = len(lst) // 2

        left, right = lst[:middle], lst[middle:]
        left_sorted = mergesort(left)
        right_sorted = mergesort(right)

        return _merge(left_sorted, right_sorted)
    
def _merge(lst1: list, lst2: list) -> list:
    """
    For use in <mergesort()> 
    Returns a sorted list from <lst1> and <lst2>
    Precondition: <lst1> and <lst2> are sorted.
    """
    slst = []
    i = 0
    ii = 0

    while i < len(lst1) and ii < len(lst2):
        if lst1[i] <= lst2[ii]:
            slst.append(lst1[i])
            i += 1
        else:
            slst.append(lst2[ii])
            ii += 1

    assert i == len(lst1) or ii == len(lst2)

    return slst + lst1[i:] + lst2[ii:]
