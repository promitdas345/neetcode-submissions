s = input()

count1 = 0
count2 = 0
count3 = 0

for ch in s:
    if ch == '1':
        count1 += 1
    elif ch == '2':
        count2 += 1
    elif ch == '3':
        count3 += 1
    

result = []
for _ in range (count1):
    result.append('1')

for _ in range (count2):
    result.append('2')

for _ in range (count3):
    result.append('3')

print('+'.join(result))

