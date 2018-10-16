"""
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')


count = 0
total = 0

while True:
    number = input('Enter a number:')
    if number == 'done':
        break
    try:
        value = float(number)
        total += value
        count += 1
    except:
        print("invalid input")
print(total, count)
print('Done!')

largest = None
smallest = None
count = 0
while True:
    array = []
    num = raw_input("Enter a number: ")
    try:
        n = float(num)
        array.append(n)
        print(array)
        if n == "done":
            for l in range(array):
                if largest is None or largest < l:
                    largest = l
                    print("Maximum", largest)
            for s in array:
                if smallest is None or smallest > s:
                    smallest = s
                    print("Minimum", smallest)
    except:
        print('Invalid input')



#Find smallest or largest
from string import digits


def main():
    user_input = ""
    smallest = largest = None
    while user_input != "done":
        user_input = input("Enter a number -> ")
        if all(l in digits for l in user_input):
            user_input = int(user_input)
            smallest = min(smallest, user_input) if smallest else user_input
            largest = max(largest, user_input) if largest else user_input
    print("Largest: {}, Smallest: {}".format(largest, smallest))


if __name__ == '__main__':
    main()


num = list()
while True:
    inp = input("Enter a number:")
    if inp == "done": break
    value = float(inp)
    num.append(value)
average = sum(num) /len(num)
print('Average:', average)
"""

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.strip()
    if line.find('From: ') >= 0:
        print(line)

