import sys

def racoon_find(dna_list):
    dna_list_seq = []
    converted_dna_list_seq = []

    dna_converter = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


    for dna_seq in dna_list:
        dna_list_seq.append(dna_seq[1])
            
        converted = []

        for index in range(int(dna_seq[0]) - 1, -1, -1):
            converted.append(dna_converter[dna_seq[1][index]])

        converted_dna_list_seq.append(''.join(converted))

    print(dna_list_seq)
    print(converted_dna_list_seq)

    indices = []

    for dna_seq in converted_dna_list_seq:
        if dna_seq in dna_list_seq:
            indices.append(dna_list_seq.index(dna_seq) + 1)

    if indices:
        print(' '.join(list(map(str, sorted(indices)))))   
    else:
        print("RACOON ROLL") 
    print()

def main():

    for _ in range(6):
        dna_list = []

        test_cases = int(sys.stdin.readline().strip())
        for _ in range(test_cases):
            dna_list.append(sys.stdin.readline().split())

        racoon_find(dna_list)

main()