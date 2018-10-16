name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

""" Get the email"""
doc = list()
counts = dict()
for line in handle:
    word = line.strip()
    if not line.startswith('From '): continue
    words = line.split()
    doc.append(words[1])

for element in doc:
    counts[element] = counts.get(element, 0) + 1
print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or bigcount < count:
        bigword = word
        bigcount = count
print("\n")
print(bigword, bigcount)
