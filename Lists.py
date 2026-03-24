if __name__ == '__main__':
        N = int(input())
        arr = []
        for i in range(N):
            inp = input().split()

            x = inp[0] if len(inp) > 0 else None
            y = int(inp[1]) if len(inp) > 1 else None
            z = int(inp[2]) if len(inp) > 2 else None


            if x == 'insert':
                    arr.insert(y, z)

            elif x == 'remove':
                    arr.remove(y)
            
            elif x == 'append':
                    arr.append(y)
                    
            elif x == 'sort':
                    arr.sort()

            elif x == 'pop':
                    arr.pop()

            elif x == 'reverse':
                    arr.reverse()

            elif x == 'print':
                    print(arr)