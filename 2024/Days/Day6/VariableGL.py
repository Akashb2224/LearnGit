global_var=20     #outside of function is global

def fun():
    local_var=10    # inside the function local
    print(local_var)
    print(global_var)

fun()

print("global variable is ", global_var)

#access global var and change the value global()
xy=200

def cool():
    global xy
    xy=100
    print(xy)

cool()
print("global var is ", xy)