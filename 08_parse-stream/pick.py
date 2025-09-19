# Wesley Leon
# Ugly Duckies
# SoftDev
# K08: Tokens in the Stream
# 2025-09-19
# time spent: 1.2
import random
u_gh = 5
duckyname = 6
with open('handles-n-quacks', 'r') as file:
    content = file.read().split('@@@')
    vals = [x.split('$$$') for x in content if x != '']
    vals = vals[1:]
    vals.sort()
    names = [x[u_gh] for x in vals if x[1] != '']
    duckiename = [x[duckyname] for x in vals if x[1] != '']

'''
We took my code because it was a easy swap to the new format.
We sanatize the data by extracing the username and duckiename pairs from the file and removing all empty usernames.
We later replace all empty ducky names with "N/A"
We seperated by @@@ as newline and $$$ as ,
'''

l = len(names)
group1 = names[:l//3]
group2 = names[l//3:(2 * l)//3]
group3 = names[(2 * l)//3:]
dgroup1 = duckiename[:l//3]
dgroup2 = duckiename[l//3:(2 * l)//3]
dgroup3 = duckiename[(2 * l)//3:]

'''
We seperated the data into thirds by using the index of the 1/3rd and 2/3rd point.
'''

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
print("sorted the names and sepearated into three groups based on index" + "\n")

group_1_member = group1[int(random.random() * len(group1))]
print("Name from first 0% - 33%:")
print(group_1_member + ':'+ dict1[group_1_member])

print("Name from first 33% - 66%:")
group_2_member = group2[int(random.random() * len(group2))]
print(group_2_member + ':'+dict2[group_2_member])

print("Name from first 66% - 100%:")
group_3_member = group3[int(random.random() * len(group3))]
print(group_3_member +':'+ dict3[group_3_member])
