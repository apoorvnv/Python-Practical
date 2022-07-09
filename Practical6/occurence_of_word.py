# Program to find occurence of a given word

def count_x(a, x):
    count = 0
    words = list(a.lower().split())
    for i in words:
        if i == x:
            count += 1
    print(("'{}' has occurred {} times").format(x, count))


a = "John had an orange orange"
count_x(a, 'orange')