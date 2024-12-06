def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # Given N array elements reverse from 3 to 7 only
    arr = [-3, 4, 2, 8, 7, 9, 6, 2, 10]
    i = 3
    j = 7
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
