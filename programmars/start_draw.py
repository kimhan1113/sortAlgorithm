





point = []

def cal(a, b):
    
    try:
        x = (a[1]*b[2] - b[1] * a[2]) / (a[0] * b[1] - b[0] * a[1])
    except:
        x = 0

    try:    
        y = -a[0] / a[1] * (a[1] * b[2] - b[1] * a[2]) / (a[0] * b[1] - b[0]*a[1])-a[2] / a[1]
        
    except:
        y = 0

    if int(x) == x and int(y) == y:
        point.append([int(x), int(y)])
    
# line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]

for i in range(len(line)):
    for j in range(i+1,len(line)):
        cal(line[i], line[j])


x = int(abs(max(list(zip(*point))[0])) + abs(min(list(zip(*point))[0]))) + 1
y = int(abs(max(list(zip(*point))[1])) + abs(min(list(zip(*point))[1]))) + 1

point = sorted(point, key = lambda x: (x[1], -x[0]), reverse=True)
print(point)

# for i in range(x):
#     for j in range(y):
#         if point[i][j]

# print(x, y)
