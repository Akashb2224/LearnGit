# start point and end point using prime num

def print_num(start,end):
    if end  > start:
        for num in range(start,end+1):
            if num > 1:
                for i in range(2,num):
                    if (num%i)==0:
                        break
                else:
                    print(num)

    else:
        

        
print_num(20,7)

