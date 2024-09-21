'''
calculating number of vowels in given string'
'''

a=0
e=0
i=0
o=0
u=0


for k in "Guvi Geeks Private Limited":
    if (k=="A" or k=="a"):
        a=1+a
    elif (k=="E" or k=="e"):
        e=1+o
    elif (k=="I" or k=="i"):
        i=1+i
    elif (k=="O" or k=="o"):
        o=1+o
    elif (k=="A" or k=="a"):
        u=1+u
    else:
        continue

print("a count-",a, "|e count-", e, "|i count -", i, "|o count-", o, "|u count -", u)