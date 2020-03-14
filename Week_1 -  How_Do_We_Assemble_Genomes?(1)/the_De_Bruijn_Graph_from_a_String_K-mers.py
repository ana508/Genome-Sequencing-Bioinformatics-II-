inpt = open('C:\\Users\\Ani\\Downloads\\dataset_200_8 (1).txt', 'r')
output = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

d = {}
reads = []

for line in inpt.readlines():
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
   output.write(key+" -> "+','.join(d[key])+'\n')
   
inpt.close()
output.close()