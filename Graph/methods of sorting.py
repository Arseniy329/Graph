def bubble_sort(arr):
    a = arr[:] 
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def quick_sort(arr):
    a = arr[:]  
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def main():
    print("Demonstration of sorting")
    raw = input("Your numbers: ")
    arr = [int(x) for x in raw.split()]

    print("\nChoose a sorting method:")
    print("1 - Bubble sort")
    print("2 - Insertion sort")
    print("3 - Selection sort")
    print("4 - Quick sort")

    choice = input("Your choise: ")

    match choice:
        case "1":
            result = bubble_sort(arr)
            method = "Bubble sort"
        case "2":
            result = insertion_sort(arr)
            method = "Insertion sort"
        case "3":
            result = selection_sort(arr)
            method = "Selection sort"
        case "4":
            result = quick_sort(arr)
            method = "Quick sort"
        case _:
            print("Try another option.")
            return

    print(f"\nMethod: {method}")
    print(f"Input list: {arr}")
    print(f"Sorted list: {result}")
    
main()
