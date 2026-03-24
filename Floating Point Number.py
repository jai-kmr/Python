def check_float(N):
    check = list(N)
    if (check[0] == '+' or check[0] == '-') and '.' in check:
        return True
    else:
        return False

if __name__ == '__main__':
    T = int(input())
    if 10>T>0:
        for i in range(T):
            N = input()
            print(check_float(N))