def capitalize(s: str):
    s = list(s)
    s[0] = s[0].upper()
    return "".join(s)

string = input()
print(capitalize(string))