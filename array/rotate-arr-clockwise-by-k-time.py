# Reverse Arr
def reverse_arr(arr, i: int, j: int):
    while (i < j):
        # swap arr[i] arr[j] without temp
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
    return arr


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    k = 4
    # Step 1 - Reverse ful array
    reverse_arr(arr, 0, len(arr)-1)
    reverse_arr(arr, 0, k)
    reverse_arr(arr, k+1, len(arr)-1)
    print(arr)
    return 0
# complexity = O(n)
# space complexity = O(1) - max_val - 4B, max_val_count - 4B


if __name__ == '__main__':
    main()
