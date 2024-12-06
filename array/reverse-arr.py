def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # Given N array elements count no of elements having atleast 1 element greater than itself
    arr = [2, 3, 10, 7, 3, 2, 10, 8, 9]
    i = 0
    j = len(arr) - 1
    print(arr)
    while (i < j):
        # swap arr[i] arr[j] without temp
        arr[j] = int(arr[j] * arr[i])
        arr[i] = int(arr[j] / arr[i])
        arr[j] = int(arr[j] / arr[i])
        i += 1
        j -= 1
    print(arr)
    return 0
# complexity = O(n)
# space complexity = O(1) - max_val - 4B, max_val_count - 4B


if __name__ == '__main__':
    main()
