# Use words.txt as the file name
"""
fname = input("Enter file name: ")
fh = open(fname)
word = fh.read()


for line in word:
    word.strip()
    print(word.upper())
    quit()

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        continue
    print('Line count:', count)

print("Done")

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
con = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    count += 1
    z = float(line[21:])
    total += z
    average = total / count
print("Average spam confidence:", average)

fname = input("Enter file name: ")
fh = open(fname)
word = fh.read()
lst = list()
for line in word:
    print(len(word))
    """
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    count += 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")




