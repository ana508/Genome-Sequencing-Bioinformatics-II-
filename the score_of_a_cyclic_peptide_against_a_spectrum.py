from collections import Counter

fin = open('C:\\Users\\Ani\\Downloads\\dataset_102_3 (3).txt','r')
fout=open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

aa = fin.readline().replace("\n","")
spectrum =  [int(i) for i in fin.read().strip().split()]
mass_table ={}
with open('C:\\Users\\Ani\\Downloads\\integer_mass_table.txt','r') as f:
    for line in f:
        pair = line.strip().split()
        mass_table[pair[0]] = int(pair[1])
        
def calculating_protein_mass(aa):
    weight = 0
    for i in aa:
        weight += mass_table[i]
    return weight

cyclospectrum = [0, calculating_protein_mass(aa)]
c_aa = aa + aa
for k in range(1, len(aa)):
	for n in range(len(aa)):
		subpep = c_aa[n:n+k]
		cyclospectrum.append(calculating_protein_mass(subpep))

m = Counter(cyclospectrum)
n = Counter(spectrum)
count = 0
for k,v in m.items():
    if k in n.keys():
        count+=min(v,n[k]) 
        
fout.write(str(count))

fin.close()
fout.close()