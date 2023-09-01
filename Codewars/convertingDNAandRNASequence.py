choose = input("rna or dna: ")
choose = choose.lower()

if choose == 'dna':
    dna = str(input("dna sequence: "))
    dnaConv = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    new_dna = str()
    for nucleotide in dna:
        new_dna += dnaConv[nucleotide]
    print(new_dna)

if choose == "rna":
    dna = str(input("rna sequence: "))
    dnaConvRna = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G' }
    new_dna = str()
    for nucleotirde in dna:
        new_dna += dnaConvRna[nucleotide]
    print(new_dna)