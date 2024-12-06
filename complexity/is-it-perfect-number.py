def is_it_perfect_num(n):
    i = 1
    factor_sum = 0
    while i * i <= n:
        if n % i == 0:
            if i == 1 or i == n / i:
                factor_sum += i
            else:
                factor_sum += i
                factor_sum += int(n / i)
        i += 1
    if factor_sum == n:
        print("YES")
    else:
        print("NO")


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    while N > 0:
        n = int(input())
        is_it_perfect_num(n)
        N -= 1
    return 0


if __name__ == '__main__':
    main()
