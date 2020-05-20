fin = open('C:\\Users\\Ani\\Downloads\\dataset_96_7 (1).txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
text = fin.readlines()
dna = text[0].replace("\n","")
peptide = text[1].replace("\n","")

def dna_codon_map():
    codon_map = {}
    with open('C:\\Users\\Ani\\Downloads\\RNA_codon_table.txt') as f:
        for line in f:
            pair = line.strip().split()
            pair[0] = pair[0].replace('U', 'T')
            if len(pair) == 2:
                codon_map[pair[0]] = pair[1]
            else:
                codon_map[pair[0]] = '*'
    return codon_map


def reverse_complement(text):
    return "".join(([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[i]
                   for i in list(text)])[::-1])
results = []
for orf in range(3):
    translated = ''.join([dna_codon_map()[dna[i:i+3]]
                          for i in range(orf, (int((len(dna)-orf)/3)*3), 3)])
    for i in range(len(translated) - len(peptide) + 1):
        if translated[i:i+len(peptide)] == peptide:
            results.append(dna[i*3+orf:i*3+orf+3*len(peptide)])

for orf in range(3):
    translated = ''.join([dna_codon_map()[reverse_complement(dna)[i:i+3]]
                          for i in range(orf, (int((len(dna)-orf)/3)*3), 3)])
    for i in range(len(translated) - len(peptide) + 1):
        if translated[i:i+len(peptide)] == peptide:
            results.append(reverse_complement(
                reverse_complement(dna)[i*3+orf:i*3+orf+3*len(peptide)]))

for i in results:
    fout.write(i+"\n")

fin.close()
fout.close()