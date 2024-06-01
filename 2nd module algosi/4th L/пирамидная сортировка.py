'''n = int(input())
l = list(map(int, input().split()))

line = []
for i in l:
    line.append(i)
    k = len(line) - 1
    while k > 0 and line[(k - 1) // 2] > line[k]:
        line[k], line[(k - 1) // 2] = line[(k - 1) // 2], line[k]
        k = (k - 1) // 2
print(line)


for i in range(n):
    line[0] = line[-1]
    k = 0
    if len(line) % 2 != 0:
        extra = len(line) // 2
    else:
        extra = (len(line) // 2) - 1
    while k < extra and line[k] < max(line[k * 2 + 1], line[k * 2 + 2]):
        if line[k * 2 + 1] < line[k * 2 + 2]:
            line[k], line[k * 2 + 2] = line[k * 2 + 2], line[k]
            k = k * 2 + 2
        else:
            line[k], line[k * 2 + 1] = line[k * 2 + 1], line[k]
            k = k * 2 + 1
    print(line)


n = int(input())
a = list(map(int, input().split()))
h = Heap()
for i in range(n):
    h.insert(a[i])
for i in range(n):
    a[-i-1] = h.extract()
print(*a)'''

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)


    for i in range(n, -1, -1):
        heapify(arr, n, i)
    print(arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)


arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print (arr[i])
