def perfect_caps(word: str):
    no_of_lowercases = 0
    list_of_letters = list(word)
    if len(word)<=1 or list_of_letters[0].isupper():
        return word
    for letter in list_of_letters:
        if letter.islower():
            no_of_lowercases+=1
    
    if no_of_lowercases>1 or no_of_lowercases<=0:
        return word
    
    list_of_letters[0] = list_of_letters[0].upper()
    for i in range(1,len(list_of_letters)):
        list_of_letters[i] = list_of_letters[i].lower()
    
    return ''.join(list_of_letters)


word = input()
print(perfect_caps(word))