
I = 1

def star():
    global I
    while I<=5:
        print("* ",end=" ")

        j=1
        while j<=5:
            print("# ",end=" ")
            j=j+1

        I=I+1
        print()

star()