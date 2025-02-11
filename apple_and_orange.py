# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where  is the start point, and  is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
# When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. *A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right. *


# s = house start
# t = house end 
# a = apple tree
# b = orange tree
# apples = distances at which each apple falls frm the tree
# oranges = distances at which each oranges falls frm the tree

def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apple = 0
    total_orange = 0
    for apple in apples:
        new_distance = a+apple
        if new_distance>=s and new_distance<=t:
            total_apple+=1
    
    for orange in oranges:
        new_distance = b+orange
        if new_distance>=s and new_distance<=t:
            total_orange+=1


    print(total_apple)
    print(total_orange)



countApplesAndOranges(75006,94961,697,97363,[-2,2,1],[5,-6])