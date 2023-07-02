# Enumerate 
# Syntax: enumerate(iterable, start=0)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

a = list(enumerate(seasons))
print("List when start at 0: ")
print(a)

print("List when start at 1: ")
b = list(enumerate(seasons, start=1))
print(b)


# def enumerate(iterable, start=0):
#     n = start
#     for elem in iterable:
#         yield n, elem
#         n += 1
# print(list(enumerate))
