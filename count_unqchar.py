'''
This file takes an argument and counts the number of unique characters in it(only alphabets for now)
'''

small_arr=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
str=input("enter string to count unique characters -")
str.casefold
print(str)
for i in small_arr: 
    if str.count(i)>0:
        print(i,"-",str.count(i))
    else:
        continue