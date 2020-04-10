with open("myfile","r") as file:
    data=file.read()
#eval needed to read dictionary straight from text file
b=eval(data)
"""
with open("C:/Users/user/Documents/myfile2","w") as myfile2:
     myfile2.write(str(b[2]))
"""
#make list from dictionary element
a=b[2]
#remove indentation
for i,value in enumerate(a):
        if a[i]=='\n':
            del a[i]
#turn back into string from list
j=''.join(a)

print(j)


     
