# 1****
# 22***
# 333**
# 4444*
# 55555
n = 5
for i in range(1, n + 1):
for j in range(1, n + 1):
if j > i:
print("*", end="")
else:
print(i, end="")
print()
