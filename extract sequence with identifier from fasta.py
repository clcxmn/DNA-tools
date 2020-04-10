with open('Annotations.genomic.txt','r') as file:
    wc=file.read()
b=[]
for i in range(0,len(wc)-1):
    if wc[i]=='6':
        if wc[i+1]=='7':
            if wc[i+2]=='9':
                if wc[i+3]=='9':
                    if wc[i+4]=='6':
                        if wc[i+5]=='3':
                            if wc[i+6]=='.':
                                if wc[i+7]=='1':
                                    n=0
                                    for k in range(i,len(wc)-1):
                                        if wc[k]=='>':
                                            n=k
                                        break
                                    for j in range(i-1,n+1):
                                        b.append(wc[j])




with open('C:/Users/user/Documents/mycontig','w') as myfile2:
     myfile2.write(str(''.join(b)))
