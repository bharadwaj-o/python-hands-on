dec= int(input("Enter your number:"))

def dec_to_oct(decimal):
    x=""
    while decimal>0:
        x= str(decimal%8) + x
        decimal//=8
    return x

print("The number in octal form is", dec_to_oct(dec))

