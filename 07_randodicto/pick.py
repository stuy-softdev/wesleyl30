# Wesley Leon
# Ugly Duckies
# SoftDev
# K07: Grab Bag
# 2025-09-17
# time spent: 1.2

import random
with open('handles-n-quacks.csv', 'r') as file:
    content = file.read().split('\n')
    vals = [x.split(',') for x in content if x != '']
    vals = vals[1:]
    vals.sort()
    names = [x[1] for x in vals if x[1] != '']
    duckiename = [x[2] for x in vals if x[1] != '']


l = len(names)
group1 = names[:l//3]
group2 = names[l//3:(2 * l)//3]
group3 = names[(2 * l)//3:]
dgroup1 = duckiename[:l//3]
dgroup2 = duckiename[l//3:(2 * l)//3]
dgroup3 = duckiename[(2 * l)//3:]


# print(group1)
# print(group2)
# print(group3)


dict1 = dict([(group1[i], dgroup1[i] if dgroup1[i] != '' else "N/A") for i in range(len(group1))])
dict2 = dict([(group2[i], dgroup2[i] if dgroup2[i] != '' else "N/A") for i in range(len(group2))])
dict3 = dict([(group3[i], dgroup3[i] if dgroup3[i] != '' else "N/A") for i in range(len(group3))])
print(dict1)
print("\n")
print(dict2)
print("\n")
print(dict3)
print("\n")
print("sorted the names and sepearated into three groups based on index")

group_1_member = group1[int(random.random() * len(group1))]
print(group_1_member, dict1[group_1_member])

group_2_member = group2[int(random.random() * len(group2))]
print(group_2_member, dict2[group_2_member])

group_3_member = group3[int(random.random() * len(group3))]
print(group_3_member, dict3[group_3_member])
