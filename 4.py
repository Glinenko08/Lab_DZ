print("Введите размерность списков (строк, столбоцов): ")
N = int(input())
M = int(input())
L = []
P = []
K = []

print("Введите (построчно) первый список L: ")
for i in range(N):
    row = []
    for j in range(M):
        e1 = int(input())
        row.append(e1)
    L.append(row)

print("Введите (построчно) второй список P: ")
for i in range(N):
    row = []
    for j in range(M):
        e2 = int(input())
        row.append(e2)
    P.append(row)

if M == N:
    for k in range(N):
        row = []
        h = 0
        while h < N:
            sume = 0
            i = 0
            j = 0
            while j < M:
                sume += L[k][j] * P[i][h]
                i+=1
                j+=1
            row.append(sume)
            h+=1
        K.append(row)
    print("Список К: ")
    print(K)
else:
    print("Произведения таких матриц не существует")