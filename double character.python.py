string=input("enter a string:")
char=string[5]
string=string.replace(char,'$')
print(char+string[:1])
