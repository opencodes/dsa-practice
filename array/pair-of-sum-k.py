def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # Given N array elements count no of elements having atleast 1 element greater than itself
    arr = [3, -2,  4, 6]
    k = 10
    # Upper Diagonal
    # for i in range(0, len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         if arr[i] + arr[j] == k:
    #             print("YES")
    #             print(f"i {i} j {j} arr[i] {arr[i]} arr[j] {arr[j]}")
    #             return
    # Lower Diagonal
    for j in range(1, len(arr)):
        for i in range(0, j):
            if arr[i] + arr[j] == k:
                print("YES")
                print(f"i {i} j {j} arr[i] {arr[i]} arr[j] {arr[j]}")
                return

    return 0
# complexity = O(n)
# space complexity = O(1) - max_val - 4B, max_val_count - 4B


if __name__ == '__main__':
    main()
