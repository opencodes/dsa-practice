def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    for i in range(1, n):
        sum = 0
        for j in range(0, len(str(i))):
            c = int(str(i)[j])
            sum += (c * c * c)
        if sum == i:
            print(i)

    return 0


if __name__ == '__main__':
    main()
