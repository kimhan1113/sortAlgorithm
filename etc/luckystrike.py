



num = input()


left = 0
right = 0

divide = len(num) // 2

for i in range(divide):
    left += int(num[i])

for j in range(divide,len(num)):
    right += int(num[j])

print(left, right)

if left == right:
    print("LUCKY")

else:
    print("READY")    