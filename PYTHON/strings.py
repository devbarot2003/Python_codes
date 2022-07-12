#Strings --> It is surrounded by single/double quotation mark.

#double quotation string

a = "Hello world!"
print(a)

#single quotation string
b = 'This is a String.'
print(b)


#Multiline String

print("\n------------Multiline String------------\n")
multiline_str = """Hello
This
Is
Multiline
String"""

print(multiline_str)

# We can also use strings as an array
print("\nCalling String as an array\n")
arr_str = "My dream is to become a Data Scientist."
print(arr_str[9])

#Concatenation of strings

print("\n------------Concatenation of strings------------\n")
st1 = "Hello"
st2 = "World!"

print(st1+" "+st2)

#String formating in python

print("\n------------String Formating in Python------------\n")
st_f1 = "Dev"
st_f2 = 19

print("My name is {}".format(st_f1))
print(f"I am {st_f2} years old.")

#Escape sequence characters in strings

print("\n------------Escape sequence characters in strings------------\n")

print("This is \'Signle Quote Escape Sequence\'")
print("This is Backslash Escape Sequence: \\")
print("This is Tab\tEscape\tSequence")
print("This is a\bBackspace Escape Sequence")
print("This is \rReturn Escape Sequence")
print("This is \fForm Feed Escape Sequence.")

#Hex Escape Sequence

print("\n------------Octal Escape Sequence------------\n")
octalValue = "\110\145\154\154\157"
print(octalValue)

#Octal Escape Sequence

print("\n------------Hex Escape Sequence------------\n")
hexValue = "\x48\x65\x6c\x6c\x6f"
print(hexValue)

print("\n\n\n\n------------STRING SLICING------------")

str_slice = "Hello This is Dev."

print(str_slice[6:15])                              # H e l l o   T h i s    i  s     D  e  v  .
                                                    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

print(str_slice[::2])                               # 0 x 2 x 4 x 6 x 8 x 10 x  12 x  14 x  16 x  (It will skip 1 word and skips to next.)


#Negative Indexing

print(str_slice[-12:-6])                            #  H   e   l   l   o       T   h   i  s       i  s     D  e  v  .
                                                    #-18 -17 -16 -15 -14 -13 -12 -11 -10 -9  -8  -7 -6 -5 -4 -3 -2 -1