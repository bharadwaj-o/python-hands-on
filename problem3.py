print("CONVERT DECIMAL NUMBERS TO OCTAL NUMBERS:")
print()
dec= int(input("Enter your number:"))

def dec_to_oct(decimal):
    x=""
    while decimal>0:
        x= str(decimal%8) + x
        decimal//=8
    return x

print("The number in octal form is", dec_to_oct(dec))

print()
print("-------------------------------------------------------")
print("REVERSE AN INTEGER:")
print()
i=int(input("Enter an integer to reverse it: "))
s1=str(i)[::-1]
i=int(s1)
print("Your integer reversed:", i)
print()
print("-------------------------------------------------------")
print("PRINT THE FIBONACCI SERIES USING THE RECURSIVE METHOD:")
print()


