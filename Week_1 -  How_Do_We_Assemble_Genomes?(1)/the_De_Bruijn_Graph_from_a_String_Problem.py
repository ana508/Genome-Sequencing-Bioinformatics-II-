inpt = open('C:\\Users\\Ani\\Downloads\\dataset_199_6.txt', 'r')
output = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
txt = inpt.readline().replace('\n','').split(' ')
k = int(txt[0])
string = inpt.readline().replace('\n','')

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
   output.write(key+" -> "+','.join(d[key])+'\n')


inpt.close()
output.close()