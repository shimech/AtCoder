def main():
    S = input()
    if 1 <= int(S[:2]) <= 12:
        if 1 <= int(S[2:]) <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= int(S[2:]) <= 12:
            print('YYMM')
        else:
            print('NA')


if __name__ == '__main__':
    main()
