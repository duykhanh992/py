fname = input('Enter file ')
if len(fname) < 1: fname = 'romeo.txt'
doc = open(fname)
lis = dict()
for line in doc:
    words = line.rstrip().split()
    print(line)
    for word in words:
        lis[word] = lis.get(word, 0) + 1
print(lis)
print("\n")
print(sorted([(v,k) for k,v in lis.items()], reverse=True))
"""
print("\n")
lst = list()
for k,v in lis.items():
    newtup = (v,k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for v,k in lst[:10]:
    print(v,k)
"""