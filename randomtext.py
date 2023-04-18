import random
import string
#random generated words will not have any meaning
def generate_random_text(num_words):
    words = []
    for i in range(num_words):
        word = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 10)))
        words.append(word)
    return ' '.join(words)

num_words = int(input("Enter the number of words you want to generate: "))
print(generate_random_text(num_words))

