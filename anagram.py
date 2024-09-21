'''
take 2 strings as argument and check if they are anagrams
'''
str1=input("Enter the first string - ")
str2=input("Enter the second string - ")
str1=str1.lower()
str2=str2.lower()

if (sorted(str1) == sorted(str2)):
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")