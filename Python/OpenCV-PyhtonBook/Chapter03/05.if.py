def main():
    year = 2020
    
    if (year % 4 == 0) and (year % 100 != 0):
        print(f'{year}는 윤년입니다.')
    elif year % 400 == 0:
        print(f'{year}는 윤년입니다.')
    else: print(f'{year}는 윤년이 아닙니다.')

if __name__ == "__main__":
    main()