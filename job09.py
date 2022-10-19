# hollow pyramid star pattern
n = int(input())

for i in range(n):
    # printing spaces
    for j in range(n - i - 1):
        print(' ', end='')

    # printing stars
    for k in range( i + 1):
        # print star at start and end of the row
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            if i == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
    print()