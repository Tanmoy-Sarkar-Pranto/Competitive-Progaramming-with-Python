from collections import Counter

string = """below the car is a rat drinking cider and bending its elbow while this thing
is an arc that can act like a cat which cried during the night caused by pain in its
bowel"""

list_of_words = string.split()

counter = {}
for word in list_of_words:
    new_word = "".join(sorted(word))
    if new_word in counter:
        counter[new_word].append(word)
    else:
        counter[new_word] = [word]

for key, value in counter.items():
    if len(value) > 1:
        print(value)