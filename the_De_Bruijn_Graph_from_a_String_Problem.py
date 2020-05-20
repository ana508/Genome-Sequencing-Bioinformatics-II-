fin = open('C:\\Users\\Ani\\Downloads\\dataset_203_7.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output1.txt', 'w')
txt = fin.readline().replace('\n','').split(' ')
k = int(txt[0])
string = fin.readline().replace('\n','')


d={}

# e == edges  n == nodes

for i in range(len(string)-k+1):
    e=string[i:i+k]
    n=string[i:i+k-1]
    if n in d.keys():
        d[n].append(e[1:])
    else:
        temp=[]
        temp.append(e[1:])
        d[n]=temp
for key in d.keys():
   fout.write(key+" -> "+','.join(d[key])+'\n')


fin.close()
fout.close()
