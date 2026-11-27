n = 25

if n % 3 == 0:
    print(n, "is divisible by 3")
else:
    print(n, "is not divisible by 3")

if n % 5 == 0:
    print(n, "is divisible by 5")
else:
    print(n, "is not divisible by 5")

n = 456
add = 0
for i in str(n):
    add = add + int(i)
print(add)
