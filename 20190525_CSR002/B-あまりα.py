def main():
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        print(A % B)


if __name__ == '__main__':
    main()
