def main():
    variable1 = 100
    variable2 = 3.14
    variable3 = -200
    variable4 = 1.2 + 3.4j
    variable5 = 'This is Python'
    
    variable6 = True
    variable7 = float(variable1)
    variable8 = int(variable2)
    
    print(f'variable1 = {variable1}, type = {type(variable1)}')
    print(f'variable2 = {variable2}, type = {type(variable2)}')
    print(f'variable3 = {variable3}, type = {type(variable3)}')
    print(f'variable4 = {variable4}, type = {type(variable4)}')
    print(f'variable5 = {variable5}, type = {type(variable5)}')
    print(f'variable6 = {variable6}, type = {type(variable6)}')
    print(f'variable7 = {variable7}, type = {type(variable7)}') #int -> float
    print(f'variable8 = {variable8}, type = {type(variable8)}') #형변환
    
if __name__ == "__main__":
    main()