'''
file handling - > it used to operform operation on the txt file or any type of the file



File handling in Python involves using built-in functions to manage data stored permanently on a disk, 
including operations like creating, opening, reading, writing, and closing files. The most common and 
recommended way to interact with files is using the with open(...) statement, which ensures the file is automatically closed, even if errors occur. 



reading - mode ('r')
write  - mode ('w', 'x', 'a')

open()
operation()
method ->
close()


read -> read data from the given file
    read() - read all data
    readline() - single line
    readlines() - return multiple lines in list 


write ->
    write() ->
        'w' mode -> add the single line data but when user add new data it override it and create new file

        'a' (append) mode -> add new data at the end and also create new file and add the data
        
        'x' mode -> create new file and add the data and if the file exist it will give the error or exception
    

    writelines()- multiple line we can write
'''



import os

# print(os.getcwd())
# #  op = D:\1315\FileHandling

# os.chdir("D:\1315\FileHandling")

# print(os.getcwd())

# op = D:\1315\FileHandling



# f = open("ex1.txt","r")
# for i in f:
#     print(i, end = "")



# f = open("ex1.txt","r")
# data = f.read(6)
# print(data)


# f = open("ex1.txt","r")

# line1 = f.readline()
# print(line1, end="")


# line2 = f.readline()
# print(line2,end="")


# line3 = f.readline()
# print(line3,end="")



# f = open("ex1.txt","r")





# f = open("ex2.txt","r")
# sum = 0
# for i in f:
#     sum = sum +(int)i
# print(sum)



# f = open("ex3.txt","w")
# f.write("the kiran academy")
# f.close()
# print()


# f = open("ex3.txt","w")
# f.writelines(["python programming batch\n","the kiram academy\n","data scince"])
# f.close()



# f = open("ex4.txt","a")
# f.write("the kiran academy")
# f.close()

# f = open("ex4.txt","a")
# f.write("karve nagar pune")
# f.close()


# f = open("ex4.txt","x")
# f.write("karve nagar pune")
# f.close()
'''
if the file exist give an error because 'x' mode create new file

  File "d:\1315\FileHandling\file.py", line 108, in <module>
    f = open("ex4.txt","x")
FileExistsError: [Errno 17] File exists: 'ex4.txt'
'''







'''

(function) def open(
    file: FileDescriptorOrPath,
    mode: OpenTextMode = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,
    opener: _Opener | None = None
) -> TextIOWrapper[_WrappedBuffer]
Open file and return a stream. Raise OSError upon failure.

file is either a text or byte string giving the name (and the path
'''



'''


(method) def write(
    s: str,
    /
) -> int
Write string s to stream.

Return the number of characters written
(which is always equal to the length of the string)
'''


'''
(method) def close() -> None
Flush and close the IO object.

This method has no effect if the file is already closed

'''



# f = open("ex5.txt","x")
# f.write("karve nagar pune")
# f.close()



'''
can not perform two operation at a time
thier are method to check the file is in which mode


readable() -> return the booelan value like true false
'''



'''
(method) def readable() -> bool
Return whether object was opened for reading.

If False, read() will raise OSError.
'''
# f = open("ex5.txt","r+")

# print(f.readable())
# print(f.writable())


# f = open("ex5.txt","a+")

# print(f.readable())
# print(f.writable())


# f = open("ex5.txt","w+")

# print(f.readable())
# print(f.writable())





# f = open("ex5.txt","wb")

# print(f.readable())
# print(f.writable())

'''
op -> 
False
True
'''


'''


tell() return the position of the cursre

seek() -> set the position
'''


f = open("ex6.txt","a")
while True:
    name = input("Enter name :")
    f.write(f'{name} \n')
    if name == 'stop':
        break