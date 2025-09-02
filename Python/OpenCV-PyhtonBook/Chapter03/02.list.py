def main():
    list1 = [1,2,3,4] #대괄호로 감쌈
    list2 = [1, 1.5, 'a', 'a', '문자열'] #다양한 자료형 사용 가능
    
    tuple1 = (1, 2) #소괄호로 감쌈
    tuple2 = (1, 1.5, 'b', 'b', '문자열') #다양한 자료형 사용 가능
    
    dict1 = {'name':'배종욱', 'email':'daum.net'} #key:value 형태
    set1, set2 = set(list1), set(list2) #집합
    
    list1[0] = 5 #리스트는 수정 삭제 추가 가능
    list2.insert(3, 'b') #원소 삽입
    #tuple1[0] = 5 리스트는 불가
    dict1['email'] = 'naver.com'
    
    print(f'list1 {list1} {type(list1)}')
    print(f'list2 {list2} {type(list2)}')
    print(f'tuple1 {tuple1} {type(tuple1)}')
    print(f'tuple2 {tuple2} {type(tuple2)}')
    print(f'dict1 {dict1} {type(dict1)}')
    print(f'set1 {set1} {type(set1)}')
    print(f'set2 {set2} {type(set2)}')
    print(f'intersection {set1 & set2}')

if __name__ == "__main__":
    main()