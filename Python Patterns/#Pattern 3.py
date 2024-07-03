# *
# **
# ***
# ****
# ***
# **
# *
size = 3
for i in range(size, -size-1, -1):
    for j in range(size, abs(i)-1, -1):
        print("*", end="")
        print()
