#실습
# 문제 1 ~ 7
jumsu = [100, 90, 100, 80, 70, 100, 80, 90, 95, 85] 
# 위 리스트는 학생번호 1번 ~ 10번까지 10명의 시험 점수이다. 

# 1. 7번의 점수를 출력하세요
print(jumsu[6])

# 2. 1번부터 5번까지의 점수를 출력하세요
print(jumsu[:5])

# 3. 4, 5, 6, 7번의 점수를 출력하세요
print(jumsu[3:7])

# 4. 짝수번째 점수를 출력하세요
print(jumsu[1::2])

# 5. 홀수번째 점수를 출력하세요
print(jumsu[::2])

# 6. 9번의 점수를 20으로 변경하고 전체 출력하세요
jumsu[8] = 20
print(jumsu[:])

jumsu2 = jumsu
print(jumsu)
print(jumsu2)
jumsu[7] = 50
print(jumsu)
print(jumsu2)
# jumsu의 8번 값을 바꾸면 jumsu2의 8번 값도 바뀐다

# 따로 처리하기 위해서는 copy라이브러리를 사용
import copy
print(jumsu)
jumsu2 = copy.deepcopy(jumsu)
print(jumsu2) # jumsu가 copy된 것을 확인
jumsu2[0] = 0
print("-" * 50)
print(jumsu)
print(jumsu2)
# 위 코드와 다르게 jumsu2의 1번 값만 변환된 것을 확인

a = 10
b = a
b = 500
print(a, b)
# immutable 원본이 바뀌지 않음 (string, 정수, 실수, 논리, 튜플)
# 변수를 이용해서 다른 변수에 대입한 다음 다른 변수에 값을 바꿔도 원본은 변하지 않음

# mutable 원본이 같이 바뀜(리스트, 셋, 딕셔너리)
# 변수를 이용해서 다른 변수에 대입한 다음 다른 변수에서 값을 바꾸면 원본도 변함

# 7. 중복된 점수는 제거하고 하나씩만 나오도록 출력하세요
jumsu = set(jumsu)
jumsu = list(jumsu)
print(jumsu)
u_jumsu = list(set(jumsu))
print(u_jumsu)

# 문제 8 ~ 9
fruits = ["복숭아", "수박", "딸기"]

# 8. fruits 리스트에 마지막 원소로 "사과", "귤"을 추가하세요
fruits.extend(["사과", "귤"])
print(fruits)
# append 함수로 하나씩 추가 하는 방법도 있음

fruits += ["복숭아", "오렌지"]
print(fruits)
# 위 코드의 방식으로 추가도 가능

# 9. fruits 리스트에서 "복숭아"를 제거하세요
fruits.remove("복숭아")
print(fruits)

# 문제 10 ~ 15
# 10. 이름, 나이 , email 주소, 취미, 결혼유무를 딕셔너리로 생성
# 취미는 2개 이상의 값을 넣는다
dic = {
    "이름" : "홍길동",
    "나이" : 20,
    "email주소" : "abc@aaa.com",
    "취미" : ["운동", "드라이브"],
    "결혼유무" : "미혼" # boolean값 가능
} 
print(dic)

# 11. 이름과 email주소를 조회해서 출력
print(dic["이름"], dic["email주소"]) # 값이 없을 때 에러
print(dic.get("email주소")) # 값이 없을 때 None

# 12. 위 딕셔너리에서 취미중 두번째 취미를 조회해서 출력하세요
hobby = dic["취미"][1]
print(hobby)

# 13. 위 딕셔너리에서 몸무게와 키 항목을 추가하세요
dic["몸무게"] = 70
dic["키"] = 180
print(dic)

# 14 딕셔너리에서 나이를 제거 하세요
del dic["나이"]
print(dic)

# 15. 딕셔너리에서 email 주소를 다른 값으로 변경하세요
dic["email주소"] = "xyz@zzz.com"
print(dic)