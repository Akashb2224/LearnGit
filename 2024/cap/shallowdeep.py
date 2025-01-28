#shallow copy perform as deep copy whe simple list


# lst=[1,2,4,5]

# lst2=lst.copy()

# lst2[2]=1000

# print(lst,lst2)     #[1, 2, 4, 5] [1, 2, 1000, 5] shallow copy works as deep copy bcoz 1 dimention list
#//////////////////////////////////////////////////////////////////////////////////////////////////////
#scenario 2 shallow copy 

# lst = [[1,2,3,4],[5,6,7,8]]

# lst2 = lst.copy()


# lst2[1][2] = 1000

# print(lst, lst2)            #[[1, 2, 3, 4], [5, 6, 1000, 8]] [[1, 2, 3, 4], [5, 6, 1000, 8]]
#//////////////////////////////////////////////////////////////////////////////////////////////////////

# Original list using deep copy 
# deep copy only update value that we mention
import  copy

lst = [[1, 2, 3, 4], [5, 6, 7, 8]]

# Deep copy of lst
lst2 = copy.deepcopy(lst)

# Modifying lst2 won't affect lst now
lst2[1][2] = 1000

print(lst, lst2)            #[[1, 2, 3, 4], [5, 6, 7, 8]] [[1, 2, 3, 4], [5, 6, 1000, 8]]