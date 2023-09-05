def spin_words(sentence):
    new_word = []    
    for word in sentence.split(' '):
        if len(word) >= 5:
            new_word.append(word[::-1])
        else:
            new_word.append(word)
    return ' '.join(new_word)

def better_spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    
print(better_spin_words("Welcome to Codewars"))