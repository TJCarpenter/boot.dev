file = "./books/frankenstein.txt"

def read(file):
    with open(file) as f:
        return f.read()

def count_letters(string):
    res = {}
    for char in string.lower():
        if char not in res:
            res[char] = 0
        res[char] += 1
    return res

def print_report(obj):
    for key in sorted(obj, key=obj.get, reverse=True):
        if key.isalpha():
            print(f"The '{key}' key was found {obj[key]} times")

              
count = count_letters(read(file))
print_report(count)
