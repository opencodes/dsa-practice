def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # Given N array elements count no of elements having atleast 1 element greater than itself
    arr = [2, 3, 10, 7, 3, 2, 10, 8]
    max_val = None
    max_val_count = 0
    for i in arr:
        if max_val == None:
            max_val = i
        if i > max_val:
            max_val = i
            max_val_count = 1

    print(f"max_val {max_val} max_val_count {max_val_count}")

    return max_val_count
# complexity = O(n)
# space complexity = O(1) - max_val - 4B, max_val_count - 4B


if __name__ == '__main__':
    main()
