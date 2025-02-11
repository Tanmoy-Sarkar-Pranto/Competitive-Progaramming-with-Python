class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all(n):
    if n == 0:
        return [None]
    if n == 1:
        return [TreeNode(0)]
    if n%2==0:
        return []
    
    res = []
    for i in range(1, n,2):
        left = all(i)
        right = all(n-i-1)
        for l in left:
            for r in right:
                node = TreeNode(0, l, r)
                res.append(node)
    
    return res


print(all(5))