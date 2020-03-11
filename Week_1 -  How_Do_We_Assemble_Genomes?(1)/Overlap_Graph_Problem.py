inpt = open('C:\\Users\\Ani\\Downloads\\dataset_198_10 (1).txt', 'r')
output = open('C:\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

reads=[]

for line in inpt.readlines():
    reads.append(line.replace('\n',''))
reads.sort()
for i in reads:
    for j in reads:
        if i[1:]==j[:len(i)-1]:
            output.write(i+' -> '+j+"\n")

inpt.close()
output.close()