print("Введите размерность списка (строк, столбоцов): ")
N = int(input())
L = []
a = 0

print("Введите (построчно) список L: ")
for i in range(N):
    row = []
    for j in range(N):
        e1 = int(input())
        row.append(e1)
    L.append(row)

i = 0
j = 0
while (i < N) & (j < N):
    for k in range(1, N-i):
        if L[i+k][j] != L[i][j+k]:
            print("Список не симметричен относительно главной диагонали")
            a += 1
    i+=1
    j+=1

if a == 0:
    print("Список симметричен относительно главной диагонали")            