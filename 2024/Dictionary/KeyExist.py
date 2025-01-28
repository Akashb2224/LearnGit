d={'suresh':56,'ramesh':33,'kishore':66,'john':77}
user=input("Enter the key to be verified: ")
if user in d:
    print("Key present in dictionary",d[user] )
else:
    print("key not present")