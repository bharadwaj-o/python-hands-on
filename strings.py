input_string=str(input("Enter the encoded string:"))
string_split=input_string.split("000")
print(string_split[0])

dict1=dict({"first_name": string_split[0], "last_name": string_split[1], "id": string_split[2]})


print(dict1)
