def is_float(N):
    try:
        float(N)
        return True
    except ValueError:
        return False
    
if __name__ == '__main__':
    T = int(input())
    if 10>T>0:
        for i in range(T):
            N = input()
            print(is_float(N))