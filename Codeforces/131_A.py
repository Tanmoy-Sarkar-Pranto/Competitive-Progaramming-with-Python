# Let's consider that a word has been typed with the Caps lock key accidentally switched on, if:
#
# either it only contains uppercase letters;
# or all letters except for the first one are uppercase.
# In this case we should automatically change the case of all letters. For example, the case of the letters that form words "hELLO", "HTTP", "z" should be changed

def perfect_caps(word: str):
    no_of_lowercase = 0
    list_of_letters = list(word)
    for letter in list_of_letters:
        if letter.islower():
            no_of_lowercase += 1

    if no_of_lowercase<=0:
        return word.lower()

    if no_of_lowercase>1:
        return word

    if list_of_letters[0].islower():
        list_of_letters[0] = list_of_letters[0].upper()
        for i in range(1,len(list_of_letters)):
            list_of_letters[i] = list_of_letters[i].lower()

    return ''.join(list_of_letters)


word = input()
print(perfect_caps(word))
