'''
This file takes a string as an argument counts the characters in the string and prints the character that has been used max
'''

small_arr=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
str=input("enter string to display maximum repeated characters -")
str.casefold
print(str)
j=[]
for i in small_arr: 
    j.insert(small_arr.index(i),str.count(i))
n=j.index(max(j))
print(small_arr[n],max(j))