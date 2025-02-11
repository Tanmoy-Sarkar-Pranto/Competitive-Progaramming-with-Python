from collections import Counter

def detect_gender(s):
    counter = Counter(s)
    if len(counter.keys())%2==0:
        return "CHAT WITH HER!"
    return "IGNORE HIM!"

string = input()
print(detect_gender(string))