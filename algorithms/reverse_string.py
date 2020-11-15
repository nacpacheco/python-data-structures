def reverse_string(string):
    if not string:
        return string
    else:
        return string[-1] + reverse_string(string[:-1])

print(reverse_string('yoyo mastery'))
