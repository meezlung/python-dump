def pig_it(text):
    final_text = []
    split = text.split()
    punctuation_marks = ['!', "#", "&", "?", ".", ",", "/", "(", ")", "~", "^", "_", "*",]

    for word in split:
        if word not in punctuation_marks:
            final_text.append(word[1:] + word[0] + "ay")
        else:
            final_text.append(word[1:] + word[0])

    return ' '.join(final_text)

print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !