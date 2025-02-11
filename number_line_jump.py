# two kangaroos, x1,x2
# jumping with each jump distance v1,v2
# check if two kangaroos can be at the same place at the same time

# Case 0: If both starting position is different but speed same, not possible
# Case 1: If x1 kangaroo starts behind x2 kangaroo and v1<=v2, then its impossible for x1 and x2 to be at the same place at the same time (vice versa)
# Case 2: If both starts at the same place but speed different, not possible (or possible? as same position at first. Don't think so)
# Case 3: if x1<x2 and v1>v2 (vice versa), then at any time if
    # i. x1>x2 = Not possible
    # ii. x1<x2 = continue jumping
    # iii. x1==x2 = possible


def kangaroo(x1, v1, x2, v2):

    if (x1<x2 and v1<v2) or (x2<x1 and v2<v1):
        return "NO"
    if x1==x2 and (v1<v2 or v2<v1):
        return "NO"
    
    if x1!=x2 and v1==v2:
        return "NO"
    
    if x1<x2 and v1>v2:
        while True:
            x1+=v1
            x2+=v2
            if x1>x2:
                return "NO"
            if x1==x2:
                return "YES"
    
    elif x2<x1 and v2>v1:
        while True:
            x1+=v1
            x2+=v2
            if x2>x1:
                return "NO"
            if x1==x2:
                return "YES"

    return "YES"


print(kangaroo(43,2,70,2))
