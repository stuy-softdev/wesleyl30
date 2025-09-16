import random
with open('handles_gh', 'r') as file:
    content = file.read().split('\n')
    names = [x for x in content if x != '']


names.sort()

group1 = names[:59//3]
group2 = names[59//3:(2 * 59)//3]
group3 = names[(2 * 59)//3:]
#print(group1)
#print(group2)
#print(group3)


dict1 = dict([(i, "Name") for i in group1])
dict2 = dict([(i, "Name") for i in group2])
dict3 = dict([(i, "Name") for i in group3])
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
