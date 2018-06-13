def to_alternating_case(string):
    new_string = ""

    for char in string:
        if char == char.upper():
            char = char.lower()
            new_string += '-'.join(char)
        else:
            char = char.upper()
            new_string += ''.join(char)

    return new_string
    #your code here
print(to_alternating_case("Hello World"))
