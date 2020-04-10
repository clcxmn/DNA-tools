with open('anno.txt','r') as file:
        data=file.read()

"""
remove everything from FASTA except, A,T,C, and G, and indents (\n) since
the file becomes practically unreadable in notepad if the whole genome is in one line
"""

li=list(data)
b=[]
for val in li:
        if val=='T':
                b.append(val)
        elif val=='A':
                b.append(val)
        elif val=='C':
                b.append(val)
        elif val=='G':
                b.append(val)
        elif val=='\n':
                b.append(val)
        else:
                pass

c=''.join(b)

with open('C:/Users/user/Documents/cleanseq','w') as data:
        data.write(str(c))
