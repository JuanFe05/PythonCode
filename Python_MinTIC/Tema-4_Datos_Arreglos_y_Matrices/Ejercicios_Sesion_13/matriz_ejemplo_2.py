def ejemplo2():
    a = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

ejemplo2()
