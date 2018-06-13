def two_sort(array):
    array.sort
    new_string = array[0]

    for c in new_string:
        c+= ''.join("***")
        new_string += ''.join(c)
    return new_string
print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
