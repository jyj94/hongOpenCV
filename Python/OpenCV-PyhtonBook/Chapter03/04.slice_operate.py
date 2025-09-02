def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'a = {a}')
    print(f'a[:2] = {a[:2]}')
    print(f'a[4:-1] = {a[4:-1]}')
    print(f'a[2::2] = {a[2::2]}')
    print(f'a[::-1] = {a[::-1]}')
    print(f'a[1::-1] = {a[1::-1]}')
    print(f'a[7:1:-2] = {a[7:1:-2]}')
    print(f'a[:-4:-1] = {a[:-4:-1]}')
    

if __name__ == "__main__":
    main()