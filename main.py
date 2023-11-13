def cocktail_sort(arr):
    comparisons = 0
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                comparisons += 1

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                comparisons += 1

        start += 1

    return comparisons


# Чтение массива из файла input.txt
with open('input.txt', 'r') as file:
    array = [int(num) for num in file.readline().split()]

# Сортировка массива методом шейкерной сортировки
comparisons = cocktail_sort(array)

# Запись отсортированного массива и числа сравнений в файл output.txt
with open('output.txt', 'w') as file:
    file.write(' '.join([str(num) for num in array]) + '\n')
    file.write(str(comparisons))
