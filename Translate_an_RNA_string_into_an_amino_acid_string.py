def rna_codon_map():
    codon_map = {}
    with open('C:\\Users\\Ani\\Downloads\\RNA_codon_table.txt') as f:
        for line in f:
            pair = line.strip().split()
            if len(pair) == 2:
                codon_map[pair[0]] = pair[1]
            else:
                codon_map[pair[0]] = '*'
    return codon_map
table = rna_codon_map()

def translate(seq):
    protein = ""
    for i in range(0,len(seq),3):
        codon = seq[i : i + 3]
        protein += table[codon]
    return protein


def read_function(seq):
    with open(seq,'r') as fin:
        text = fin.read().replace("\n","").replace("\r","")
    return text

dna = read_function('C:\\Users\\Ani\\Downloads\\dataset_96_4 (1).txt')

fout=open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
fout.write(translate(dna)[:-1])
fout.close()