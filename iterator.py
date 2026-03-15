'''
Iterator in python ->
    In Python, an iterator is an object that represents a stream of data and provides a way to access elements one at a time
    while keeping track of the current position. Iterators are memory-efficient, especially when dealing with large datasets or
    infinite sequences, because they only load one item into memory at a time.




   1. __iter__(): This method is called to initialize the iterator and must return the iterator object itself.

   2. __next__(): This method is called to retrieve the next item from the sequence. It must raise a StopIteration exception
    when there are no more items to return, signaling the end of the iteration.
'''
my_list = [10, 20]
my_iterator = iter(my_list) # Get iterator from iterable
print(next(my_iterator))    # Output: 10
print(next(my_iterator))    # Output: 20
# next(my_iterator)         # Raises StopIteration



# 1. Start with an iterable (a list)
my_fruits = ["apple", "banana", "cherry"]

# 2. Convert it into an iterator
fruit_iterator = iter(my_fruits)

# 3. Use next() to get items one by one
print(next(fruit_iterator))  # Output: apple
print(next(fruit_iterator))  # Output: banana
print(next(fruit_iterator))  # Output: cherry




class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.high:
            num = self.current
            self.current += 1
            return num
        else:

            raise StopIteration
my_counter = Counter(1, 3)

for n in my_counter:
    print(n)
