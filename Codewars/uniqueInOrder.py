# type: ignore

def unique_in_order(sequence):
    tracker = ""
    final_answer = []
    for seq in sequence:
        if seq != tracker:
            final_answer.append(seq)
            tracker = seq
    return(final_answer)

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))