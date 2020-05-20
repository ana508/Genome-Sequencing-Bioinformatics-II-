mass_table ={}
with open('C:\\Users\\Ani\\Downloads\\integer_mass_table.txt') as f:
    for line in f:
        pair = line.strip().split()
        mass_table[pair[0]] = int(pair[1])

def read_function(seq):
    with open(seq,'r') as fin:
        text = fin.read().replace("\n","").replace("\r","")
    return text
fout=open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
# amino acid sequence == aa
aa =  read_function('C:\\Users\\Ani\\Downloads\\dataset_98_4.txt')

def calculating_protein_mass(aa):
    total_weight = 0
    for i in aa:
        total_weight += int(mass_table[i])
    return total_weight

cyclospectrum = [0, calculating_protein_mass(aa)]
c_aa = aa + aa
for k in range(1, len(aa)):
	for n in range(len(aa)):
		subpep = c_aa[n:n+k]
		cyclospectrum.append(calculating_protein_mass(subpep))

fout.write(' '.join(map(str, sorted(cyclospectrum))))
fout.close()