"""
Function returns sub-sequences of a chosen length (le) within intervals of a
chosen length (itvl) across an entire sequence/scaffold (scaf) organized in
a list format in order from the beginning to the end of the scaffold

saves list into desired directory as string
"""

#replace 'cleanseq' with sequence of choice, file goes in same folder as program
with open('cleanseq','r') as file:
    data=file.read()

def scaf_survey(scaf,le,itvl):
    b={}
    for i in range(0,len(scaf)-1):
        if i%itvl==0:
            c=[]
            for j in range(i,i+le):
                c.append(scaf[j])
                b[int(i/itvl)]=c
    d=[]
    for i in b:
        b[i].append('\n\n\n')
        d.append(''.join(b[i]))
    with open('C:/Users/user/Documents/post_survey','w') as data:
        data.write(str(d))


scaf_survey(data,1000,10000)

