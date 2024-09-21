'''
This program reads input and removes the vowels"
'''
str=input("Enter the string for vowel stripping -")

for k in str:
    if (k=="A" or k=="a"):
        str=str.replace(k,"")
    elif (k=="E" or k=="e"):
        str=str.replace(k,"")
    elif (k=="I" or k=="i"):
        str=str.replace(k,"")
    elif (k=="O" or k=="o"):
        str=str.replace(k,"")
    elif (k=="A" or k=="a"):
        str=str.replace(k,"")
    else:
        continue

print(str)
