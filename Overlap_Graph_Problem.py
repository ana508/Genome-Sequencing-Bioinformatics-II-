fin = open('C:\\Users\\Ani\\Downloads\\dataset_198_10.txt', 'r')
fout = open('C:\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

reads=[]

for line in fin.readlines():
    reads.append(line.replace('\n',''))
reads.sort()
for i in reads:
    for j in reads:
        if i[1:]==j[:len(i)-1]:
            fout.write(i+' -> '+j+"\n")

fin.close()
fout.close()