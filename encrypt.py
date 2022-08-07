name=input("Please enter your name: ")
print("Welcome, "+name)
print("What would you like to do?: \n1. Encrypt password \n2. Decrypt Password")
num=int(input("Enter the correct number: "))

while num!=1 and num!=2:
    num=int(input("Enter the correct number: "))

if num==1:
    plain=input("Enter your password: ")
    key=int(input("Enter encryption key: "))
    cypher=""
    for char in plain:
        midway=ord(char)
        new_num=(midway+key)%144697 #This is the number of characters currently in unicode
        # Use new number to get new letter and add it to cypher
        cypher=cypher+chr(new_num)
    print("Encrypted password is: "+cypher)
else:
    cypher=input("Enter encrypted password: ")
    key=int(input("Enter decryption key: "))
    plain=""
    for char in cypher:
        midway=ord(char)
        new_num=(midway-key)%144697
        plain=plain+chr(new_num)
    print("Decrypted password is: "+plain)