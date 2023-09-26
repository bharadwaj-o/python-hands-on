input_string=str(input("Enter the encoded string:"))
str1=""
strspl=list()
for i in input_string:
    if i!="0":
        str1=str1+i
    elif input_string[input_string.index(i)-1]!=0:
        if str1!="":
            strspl.append(str1)
        else:
            continue
        str1=""
    elif input_string[input_string.index(i)-1]==0:
        str1=""
strspl.append(str1)
print(strspl)


    
