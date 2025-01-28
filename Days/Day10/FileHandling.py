#writing data in text file

file=open("C:\Python prog\Day10\Demofile\demotxt",'w')

file.write("this is my 1 statement...\n")
file.write("this is my 2 statement...\n")
file.write("this is my 3 statement...\n")
file.write("this is my 4 statement...\n")
file.close
print('writing program completed')


#example 2 read data from text file
file=open("C:\Python prog\Day10\Demofile\demotxt",'r')

print(file.read())

file.close 

print('reading file completed')

#example append data in existing text file
file=open("C:\Python prog\Day10\Demofile\demotxt",'a')

file.write('this is my 5 line...\n')
file.write('this is my 6 line...\n')
file.write('this is my 7 line...\n')

file.close
print('append completed')

file=open("C:\Python prog\Day10\Demofile\demotxt",'r')
data=file.read()
new_data=data.replace("4","44")
print(new_data)
file.close
print('Replace completed')