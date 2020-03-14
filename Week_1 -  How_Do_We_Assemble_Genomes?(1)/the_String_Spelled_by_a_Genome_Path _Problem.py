inpt = open('C:\\Users\\Ani\\Downloads\\dataset_198_3.txt', 'r')
output = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
reads=[]

for line in inpt.readlines():
    reads.append(line.replace('\n',''))

k=len(reads[0])
output.write(reads[0])

for r in reads[1:]:
    output.write(r[k-1:])
    
inpt.close()
output.close()
