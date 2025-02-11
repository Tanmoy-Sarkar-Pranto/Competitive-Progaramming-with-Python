from collections import Counter

def read_data():
    return int(input())

def read_data_multiple(n):
    return [int(x) for x in input().split(" ")][:n]


def check_breaking_condition(counter: Counter)->bool:
    for i in counter.keys():
        if counter[i]>0:
            return False
    return True

# 5, [1,2,4,3,3]
# total_taxis = 0, space_remaining=4, 


def taxi(n, groups):
    counter = Counter(groups)
    total_taxis = counter[4] + counter[3] + counter[2]//2
    counter[1]-=counter[3]
    if counter[2]%2==1:
        total_taxis+=1
        counter[1]-=2
    if counter[1]>0:
        total_taxis += (counter[1]+3)//4
    return total_taxis

n = read_data()
groups = read_data_multiple(n)

print(taxi(n, groups))