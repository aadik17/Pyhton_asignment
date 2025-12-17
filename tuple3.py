
t = (1, 2, 2, 3, 2, 4)
target = 2
count = 0

for x in t:
    if x == target:
        count += 1

print("Tuple:", t)
print(f"Occurrences of {target}: {count}")
