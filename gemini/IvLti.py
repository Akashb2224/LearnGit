# def shortar():

#     arr1 = [1,4,6,8]
#     arr2 = [3,5,6,7]


# arr3=arr1.extend(arr2);
# print(arr3)
# for I in arr3():
# 	if I != len(arr3):
#         elif I <= I+1:
# 	    	arr3.remove(I);
# 		    arr3.append(I);
# 		    I +=1;
# 	else:
# 		return
# print(arr3);



def shortar():
    arr1 = [1, 4, 6, 8]
    arr2 = [3, 5, 6, 7]

    # Merge the two arrays
    arr1.extend(arr2)

    # Sort the merged array
    arr1.sort()
    print("sorted array: ",arr1)

    # Remove duplicates
    arr3 = []
    for i in arr1:
        if i not in arr3:
            arr3.append(i)
        else:
            print("duplicate element in array is :",i)
    return arr3

# Example usage
result = shortar()
print(result)
