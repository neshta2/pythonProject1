arr_2d = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def print_matrix(arr_2d):  # вывод массива с новой строки
    for arr in arr_2d:
        for el in arr:
            print(el, end=' ')
        print()


print_matrix(arr_2d)


def create_2d_arr(m, n):
    arr_2d = []
    for i in range(m):
        internal_arr = []
        for j in range(n):
            internal_arr.append(0)
        arr_2d.append(internal_arr)
    return arr_2d


arr_5_10 = create_2d_arr(5, 10)
print_matrix(arr_5_10)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j]=temp

def mirror_2d_arr(arr_2d):
    for arr in arr_2d:
        for i in range(len(arr) // 2):
            swap(arr, i, len(arr) - 1 - i)
print_matrix(arr_2d)
print(" ")
mirror_2d_arr(arr_2d)
print_matrix(arr_2d)