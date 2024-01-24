# set = it's a list but unordered, unindexed and can't have duplicate values

set  = {"fork", "knife", "knife", "spoon"}
dishes = {"bowl", "plate", "cup", "knife"}

#set.add("napkin")
#set.remove("fork")
#set.clear() 
#set.update(dishes)
#dishes.update(set)

'''set[0] = "banana"
print(set[0]) --> Those doesn't work'''

dinner_table = set.union(dishes)

for i in set:
   print(i)

print()
print(dishes.difference(set))
print(dishes.intersection(set))
print()

#for i in dinner_table:
 #   print(i)'''