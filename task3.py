text = "Before departure, all students leaving for exchange studies should fill in a specialized application form. An application should be submitted in 1 copy and not later than 2 weeks prior to departure for the exchange semester, provided that the students do not have any academic failure. The paper should be submitted to the International Academic Mobility Office (Volkhovsky per., 3, office 207, Tel.: +7 (812) 323 8447). A copy of the invitation letter from a host school - partner of GSOM SPbU has to be attached to the application."

address = text.split("(")[1].split(", Tel.")[0]
print(address)

begin = text.find("(")+1
ideally = text[begin:text.find(", Tel.", begin)]
print(ideally)

# lists

list1 = ["aaa", "bb", "c"]
list2 = list((1, 25, 33))
list3 = [i for i in range(15)]

print(list1, list2, list3, sep = "\n")

list1.insert(1, "d")
list1.append("z")
print(list1)
list1.sort()
print(list1)
list1.sort(key = lambda x: len(x))
print(list1)
list2.extend(list1)
print(list2)
print("bb index =", list2.index("bb"))
print("list2 length =", len(list2))

list4 = list2
list4.pop()
print(list2, list4, sep= "\n")

import copy

list5 = copy.deepcopy(list4)
print(list5, "\n")
list5.pop()
print(list4, "\n", list5, "\n", sep = "")
list5.reverse()
print(list5)

print(max(list3))
print(min(list3))
print(sum(list3))
print(len(list3))
print((list3))
print(list3[2:10])
list3[1:2] = [55,22]
print(list3)

# tuples

tup = (1, 33, 22, [11, 22])
print(min(tup[:3]))
print(max(tup[:3]))
print(len(tup[:3]))
print(sum(tup[:3]))

tup[3][0] = 43

print(tup)

# dictionaries

keys = ["a", "b", "c", "d", "f"]
values = [22, 3, 43, 12, 32]
d = dict()
for k,v in zip(keys, values):
    d[k] = v

print(d)

d1 = {"a": 12, "b": "cat", "c": [32, 22], "d": (23, 22)}

print(d.keys())
print(d.values())
print(max(d))
print(max(d.values()))
print(d.items())
d.update({"e": 97})
d.pop("a")
print(d)

print(d["b"] + d["c"])
print(d1["c"])
d1["c"][0] = 1
print(d1)

# sets

s1 = set([1,2,3, 3, 1, 1, 1, 32])
s2 = set((1, 2, 3, 33, 3, 1, (1, 2), (1, 2)))
print(s1, s2)
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)

s1.add(1)
print(s1)
s1.discard(32)
print(s1)

s2 = set((1, 2, 3, 33, 3, 1, (1, 2), [1, 2]))