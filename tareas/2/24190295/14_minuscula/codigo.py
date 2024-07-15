
string = input()

s = ""
for char in string: 
    if 'A' <= char <= 'Z':
       s += chr(ord(char) + 32)  
    else:
     s += char

print(s)

