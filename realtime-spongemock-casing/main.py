import random
import sys

def spongecase(word, random_counter):
    word_list = list(word)

    for index in range(len(word_list)):
        random_number = random.randint(1, random_counter)
        if (index + 1) % random_number == 0: # To check if that certain index is divisible by the random number
            word_list[index] = word_list[index].upper()

    print(''.join(word_list))

def spongecase_using_head_tails(word, half=0.5):
    spongecase_word = []

    for letter in word:
        random_value = random.random() # Heads or Tails but 1s and 0s
    
        if random_value < half:
            spongecase_word.append(letter.upper())
        else:
            spongecase_word.append(letter.lower())

    print(''.join(spongecase_word))

if len(sys.argv) == 2:
    input_word = sys.argv[1]
else:
    print("Please enter a valid input.")

# spongecase(input_word)
spongecase_using_head_tails(input_word)
