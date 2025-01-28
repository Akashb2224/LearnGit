import random

lst = [random.randint(0, 100) for i in range (10)]
print("list befor swapping",lst)

N=5
if len(lst) >= 2 * N:
    lst[-N:],lst[:N]=lst[:N],lst[-N:]
else:
    print("List is not long enough to swap.")

print("list after swapping is :",lst)


