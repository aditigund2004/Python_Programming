'''
Patterns printing in python 
'''
# #Example 1
# for r in range(1,6):
#     for c in range(1,6):
#         print("*",end=" ")
#     print()   

# #example 2     
# for r in range(1,11):
#     for c in range(1,7):
#         print("*",end=" ")
#     print()

# #Example 3
# for r in range(1,7):
#     for c in range(1,4):
#         print("*",end=" ")    
#     print()    

# #Example 4  
# for r in range(1,4):
#     for c in range(1,7):
#         print("*",end=" ")    
#     print()  

# #Example 5
# for r in range(1,6):
#     for c in range(1,6):
#         print(c,end =" ")
#     print() 

# #Example 6
# for r in range(1,3):
#     for c in range(1,7):
#         print(c,end =" ")
#     print()        

# #Example 7
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()    

# #Example 8
# for i in range(1,5):
#     for j in range(5, 0, -1):
#         print(j, end=" ")
#     print()
    
# #Example 9
# for r in range(5, 0, -1):
#     for c in range(1,5):
#         print(r, end=" ")
#     print()

'''
Introduction to some functions
'''
# t1 = 'X'
# print(t1)
# a1=ord(t1)  #To find the unicode of the character(ord){character --> Number}
# print(a1)
# print(ord('a'))

# t1 = 97
# print(t1)
# a1=chr(t1)  #To find the character with the help of unicode(chr){Number  --> Character}
# print(a1)
# print(chr(90))

# #Example 10 
# for r in range(1,6):
#     for c in range(65,70,1):
#         print(chr(c),end =" ")
#     print()    

# #Example to print the character patterns
# ch1 = 'A'
# for r in range(1,6):
#     code = ord(ch1)
#     for c in range(1,6):
#         print(chr(code),end = " ")
#         code = code +1
#     print()    

# #Example
# ch1 = 'a'
# for r in range(1,6):
#     code = ord(ch1)
#     for c in range(1,6):
#         print(chr(code),end = " ")
#         code = code +1
#     print()        

# #Example
# for r in range(1,6):
#     for c in range(97,102):
#         print(chr(c),end = " ")
#     print()        

# #Example 
# for r in range(65,70):
#     for c in range(1,6):
#         print(chr(r),end = " ")
#     print()    

# #Example 
# for r in range(69,64,-1):
#     for c in range(1,6):
#         print(chr(r),end = " ")
#     print()       


# ch1 = 'a'
# code = ord(ch1)
# for r in range(1,6):
#     for c in range(1,6):
#         print(chr(code),end = " ")
#     code = code +1
#     print() 

# ch1 = 'E'
# code = ord(ch1)
# for r in range(1,6):
#     for c in range(1,6):
#         print(chr(code),end = " ")
#     code = code -1
#     print()            


# for r in range(1,6):
#     for c in range(69,64,-1):
#         print(chr(c),end = " ")
#     print() 

# ch1 = 'E'
# for r in range(1,6):
#     code = ord(ch1)
#     for c in range(1,6):
#         print(chr(code),end = " ")
#         code = code - 1
#     print()            

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if c ==3:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print()    
          
# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if r ==3:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print()          

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if r ==3 or c==3:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print() 

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if c==1 or c==5:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print() 

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if r==1 or r==5:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print() 

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if (c==1 or c==5) or (r ==1 or r ==5):
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print() 

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if (c==1 or c==5) or (r ==1 or r ==5):
#             print("*",end = " ")
#         else:    
#             print("$",end = " ")
#     print()

# #Example
# for r in range(1,6):
#     for c in range(1,6):
#         if c==r:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     print()  

# #Example
# i = 5
# for r in range(1,6):
#     for c in range(1,6):
#         if c==i :
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     i = i -1        
#     print()  

# #Example
# i = 5
# for r in range(1,6):
#     for c in range(1,6):
#         if c==i or c==r:
#             print("$",end = " ")
#         else:    
#             print("*",end = " ")
#     i = i -1        
#     print()


#Example
for r in range(1,6):
    for c in range(1,6):
        if r==c or r+c==6:
            print("$",end = " ")
        else:    
            print("*",end = " ")        
    print()