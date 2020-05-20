fin = open('C:\\Users\\Ani\\Downloads\\dataset_104_4.txt', 'r')
fout=open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
spectrum=[int(x) for x in (fin.readline().split(' '))]
spectrum.sort()
c=[]
for i in spectrum:
    for j in spectrum:
        if i-j>0:
            c.append(i-j)
fout.write(' '.join(map(str,c)))

fin.close()
fout.close()