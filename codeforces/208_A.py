def dubstep(s):
    list_of_words = s.split("WUB")
    new_word = ' '.join(list_of_words).strip().split()
    return " ".join(new_word)

s = input()
print(dubstep(s))