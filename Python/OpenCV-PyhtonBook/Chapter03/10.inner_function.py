def main():
    a = [1.5, 2, 3, 4, 5]
    b = map(float, a)
    c = divmod(5, 3)
    
    print(f'max = {max(a)}, min = {min(a)}')
    print(f'몫과 나머지 : {c}')
    print(f'type of c : {type(c)}, c[0] = {type(c[0])}, c[1] = {type(c[1])}')
    print(f'2^4 = {pow(2, 4)}')
    print(f'절대값 = {abs(-4)}')

if __name__ == "__main__":
    main()