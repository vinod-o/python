
def reverse_string(txt):
    reverse = ' '
    for char in txt:
        reverse = char + reverse
    return reverse
print(reverse_string('hello'))
