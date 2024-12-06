def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    n = int(input())
    c = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            if i == 1 or i == n / i:
                c += 1
                print(f"factor {i} - c {c}")
            else:
                c += 2
                print(f"factor {i} {n / i} - c {c}")
        if c > 2:
            print("NO")
            return
        i += 1
    print("YES")
    return 0


if __name__ == '__main__':
    main()
