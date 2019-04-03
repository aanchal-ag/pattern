tset=[1,3,5,7,8,0,10]
print(tset)
print(tset[3])
tset.append(6)
print(tset)
tset.insert(1,9)
print(tset)
tset.remove(5)
print(tset)
n=["a","b","c","d"]
n.append(6)
print(n)
print(n*2)
tset.remove(0)
print(tset)
t=tset.index(10)

print(t)
for x in n:
    print(x)
tset[1]=78
print(tset)
if 7 in tset:
    print("present")
else:
    print("not present")
print(n+n)
print(len(n))
del n[1]
print(n)
n.clear()
print(n)
n=["a","b","c","d"]
t=n.copy()
print(t)
n.pop()
print(n)
print(tset[2:6])

