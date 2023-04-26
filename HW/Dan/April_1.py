# 1
for i in range(0, int(input())):
    string = input()
    counters = [0, 1, 1]
    result = True
    for j in range(0, len(list(string))-1):
      if result:
        if string[j] == string[j+1]:
            if counters[0] % 2 == 0:
                counters[1] += 1
            else:
                counters[2] += 1

        elif string[j] != string[j+1]:
            if counters[0] % 2 == 1 and string[0] != 0:
                if counters[1] != counters[2]:
                    result = False
                counters[1] = 1

            elif counters[0] % 2 == 0 and string[0] != 0:
                if counters[1] != counters[2]:
                    result = False
                counters[2] = 1
            counters[0] += 1
    if result:
        print("YES")
    else:
        print("NO")

# 2
def is_simpatic(table):
    n = len(table)
    m = len(table[0])
    for i in range(n - 1):
        for j in range(m - 1):
            if table[i][j] == table[i+1][j] == table[i][j+1] == table[i+1][j+1]:
                return False
    return True


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    table = []
    for i in range(n):
        row = list(map(int, input().split()))
        table.append(row)
    if is_simpatic(table):
        print("YES")
    else:
        print("NO")

