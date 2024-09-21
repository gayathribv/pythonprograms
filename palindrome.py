'''
Check if the string entered is a plaindrome or not
'''
str=input("Enter String to be checked for palindrome - ")
length=len(str)//2
i=0
j=length
while i <= length//2:
    while j >= length//2:
        if str[i] == str[j]:
            pal="yes"
            i=i+1
            j=j-1
        else:
            pal="no"
            i=i+1
            j=j-1


if pal == "yes":
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")
