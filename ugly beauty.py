num = int(input())
for i in range(num):
    n = int(input())
    a = list(map(int, input().strip().split()))[:n]
    # li= list(a.sort())
    # print(a.sort())
    if (a == sorted(a)):
        print("ugly")
    else:
        for j in range(n):
            if (a.count(a[i]) == 1):
                continue
            else:
                print("ugly")
                break
        print("beautiful")


