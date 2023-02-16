# Python Iterators
# Return an iterator from a tuple
mytup = ("apple", "banana", "cherry")
myit = iter(mytup)
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
# Iterate the values of a tuple
mytup = ("apple", "banana", "cherry")
for i in mytup:
    print(i)

# Iterate the characters of a string
mystr = "banana"
for i in mystr:
    print(i)

# Create a iterator that reuturns numbers
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    

    def __next__(self):
        x = self.a
        self.a += 1
        return x

    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

