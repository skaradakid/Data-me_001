# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    rev_lst = lst[::-1] # Implement this
    return rev_lst


def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    count = 0  # Implement this
    for x in lst:
        if x == element:
            count += 1
    return count

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    lst = []
    for x in dct: # Implement this
        if dct[x] == value:
              lst.append(x)
    return(lst)


def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    s_lst1 = sorted(lst1)# Implement this
    s_lst2 = sorted(lst2)
    lst3 = s_lst1 + s_lst2
    s_lst3 = lst3
    return sorted(s_lst3)
print(merge_sorted_lists([1,3,46,4,6,3,77,7], [-1,3,4,5,654,134,-123]))

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    sort_numbers = sorted(numbers)  # Implement this
    if len(numbers) <= 1:
        return None
    elif sort_numbers[-1] == sort_numbers[-2]:
        return None
    else:
        return sort_numbers[-2]

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    for x in str1:   # Implement this
        if x in str2:
            continue
        else:
            return False
    return True


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    flat_list = []  # Implement this
    for x in nested_list:
        for y in x:
            flat_list.append(y)

    return flat_list


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    set_list = set(lst)  # Implement this
    new_list = list(set_list)
    return new_list

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    common_list = []  # Implement this
    for x in lst1:
        if x in lst2:
            common_list.append(x)
    return common_list