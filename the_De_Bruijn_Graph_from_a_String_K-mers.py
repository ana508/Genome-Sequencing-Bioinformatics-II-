fin = open('C:\\Users\\Ani\\Downloads\\dataset_203_7.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output1.txt', 'w')

d = {}
reads = []

for line in fin.readlines():
    reads.append(line.replace('\n',''))

# e == edges  n == nodes

for i in reads:
    e = i
    n=i[:len(i)-1]
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