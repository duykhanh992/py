from __future__ import annotations
import re
"""
x = 'From: Using the: character'
y = re.findall('^F.+', x)
print(y)


name = input("Enter File:")
if len(name) < 1:name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line.rstrip()
    if re.search('^From:', line):
        print(line)

name = input("Enter file:")
if len(name) < 1: name = "Sample_sum.txt"

handle = open(name)
lis = list()
count = 0
for line in handle:
    line.rstrip()
    y = re.findall('[0-9]+', line)
    if y == []:continue
    lis.append(y)
for i in lis:
    for z in i:
        count += int(z)
print(count)
"""
name = input("Enter file:")
if len(name) < 1: name = "Actual_sum_42.txt"

handle = open(name)
lis = list()
count = 0
for line in handle:
    line.rstrip()
    print(line)
    y = re.findall('[0-9]+', line)
    if y == []:continue
    lis.append(y)
for i in lis:
    for z in i:
        count += int(z)
print(count)