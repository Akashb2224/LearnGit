# inputs

# x=[a,b,c,d,e] and
# y =[1,2,3,4]



# output array  
# op=[a,1,b,2,c,3,d,4,e]


x=['a','b','c','d','e'] 
y =[1,2,3,4]

op=[]

for i in range(len(y)):
    
    op.append(x[i])
    op.append(y[i])

print(op)