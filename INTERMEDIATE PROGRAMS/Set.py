set = {5,50,99,66,64,8,6,97}
set.add(444)# add given element
print(set)
set.remove(50)# raise error if not found element
print(set)
set.discard(1)# not raise error if not found element
print(set)
set1 = {8,5,4,99,66}
print(set.intersection(set1))
print(set.union(set1))
print(set.difference(set1))