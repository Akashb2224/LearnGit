# Approch 1 using 3rd variable

d1={'suresh':56,'ramesh':33,'kishore':66,'john':77}
sm=0
for i in d1:
    sm=sm+d1[i]
print(sm)

#Approch 2 using sum() method
total=sum(d1.values())
print("using sum method",total)