def main():
    kor = [70, 80, 90, 40, 50]
    eng = [90, 80, 70, 70, 60]
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    
    for i in range(0, 5): 
        sum1 = sum1 + kor[i] + eng[i]
        
    for k in kor:
        sum2 = sum2 + k
    for e in eng:
        sum2 = sum2 + e
        
    for i, k in enumerate(kor):
        sum3 = sum3 + k + eng[i]
        
    for k, e in zip(kor, eng):
        sum4 = sum4 + k + e
        
    print(f'sum1 = {sum1}')
    print(f'sum2 = {sum2}')
    print(f'sum3 = {sum3}')
    print(f'sum4 = {sum4}')

if __name__ == "__main__":
    main()